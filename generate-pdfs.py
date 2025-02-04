import os
import requests
import certifi
import pandas as pd
import json
from lxml import html
import xml.etree.ElementTree as ET
from pytrustnfe.certificado import Certificado
from pytrustnfe.nfse.ginfes import consultar_nfse_por_rps
import re
import time
import unicodedata

def sanitize_filename(name):
    name = name.strip()
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    name = re.sub(r'[^\w\-]', '_', name)
    name = name.lower()
    return name

def download_note_pdf(verification_id, note_number, file_name, output_dir="output"):
    session = requests.Session()
    session.verify = certifi.where()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    })

    consulta_url = "http://visualizar.ginfes.com.br/report/consultarNota"
    params = {
        "__report": "nfs_ver15",
        "cdVerificacao": verification_id,
        "numNota": str(note_number),
        "cnpjPrestador": "null"
    }

    formulario_url = "http://visualizar.ginfes.com.br/report/exportacao"

    os.makedirs(output_dir, exist_ok=True)

    try:
        response = session.get(consulta_url, params=params)
        response.raise_for_status()

        tree = html.fromstring(response.content)
        form = tree.xpath("//form[@name='exportar']")
        if not form:
            raise ValueError("Export form not found.")

        form_data = {input_tag.attrib.get('name'): input_tag.attrib.get('value', '')
                     for input_tag in form[0].xpath(".//input")}
        form_data.update({'imprime': '0', 'tipo': 'pdf'})

        post_response = session.post(formulario_url, data=form_data, stream=True)
        post_response.raise_for_status()

        if 'application/pdf' not in post_response.headers.get('Content-Type', ''):
            raise ValueError("The response is not a PDF file.")

        output_path = os.path.join(output_dir, file_name)
        with open(output_path, 'wb') as file:
            for chunk in post_response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"PDF saved at: {output_path}")

    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # listing notes to download
    filename = '/Users/addo/Downloads/teste_emissao_nf_pdf.xlsx'
    df = pd.read_excel(filename, skiprows=1)


    certificado = open("/Users/addo/jobs/addodelgrossi/go-nfs-e/resources/35143637000111.pfx", "rb").read()
    certificado = Certificado(certificado, b'k4ex2018')

    previous_serie = None
    index = 1
    for _, row in df.iterrows():
        current_serie = row['SERIE']

        if current_serie != previous_serie:
            index = 1  # Reset index when SERIE changes
            previous_serie = current_serie
        else:
            index += 1

        obj = {
            'cnpj_prestador': row['CNPJ'],
            'inscricao_municipal': row['INSCRICAO'],
            'numero': str(index),
            'serie': str(current_serie),
            'tipo': '1'
        }

        resposta = consultar_nfse_por_rps(certificado, consulta=obj, ambiente='producao')
        try:
            root = ET.fromstring(resposta['received_xml'])
            namespaces = {
                'ns3': 'http://www.ginfes.com.br/servico_consultar_nfse_rps_resposta_v03.xsd',
                'ns4': 'http://www.ginfes.com.br/tipos_v03.xsd'
            }

            codigo_verificacao = root.find('.//ns4:CodigoVerificacao', namespaces).text
            numero = root.find('.//ns4:Numero', namespaces).text
            data_emissao = root.find('.//ns4:DataEmissao', namespaces).text.split('T')[0]  # Extract date part

            data_emissao_formatted = data_emissao.replace('-', '')
            fantasia_sanitized = sanitize_filename(row['FANTASIA'])
            file_name = f"{data_emissao_formatted}_{row['ID']}_{fantasia_sanitized}_nf.pdf"

            # Call the download_note_pdf function
            download_note_pdf(
                verification_id=codigo_verificacao,
                note_number=numero,
                file_name=file_name
            )

            print('waiting 3 seconds...', fantasia_sanitized)
            time.sleep(3)


        except ET.ParseError as e:
            print(f"XML Parse Error for row ID {row['ID']}: {e}")
        except AttributeError as e:
            print(f"Missing XML elements for row ID {row['ID']}: {e}")
        except Exception as e:
            print(f"An error occurred while processing row ID {row['ID']}: {e}")
