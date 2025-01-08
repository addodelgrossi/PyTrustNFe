import requests
import ssl
import os

from lxml import html
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
import certifi


# Configura a sessão
session = requests.Session()
session.verify = False  # Desativa a verificação SSL (usar apenas se necessário)

# Adiciona headers para simular um navegador
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
})

# Parâmetros fornecidos
url_consulta = "http://visualizar.ginfes.com.br/report/consultarNota"
params = {
    "__report": "nfs_ver15",
    "cdVerificacao": "SJWOPKQH7",
    "numNota": "2405",
    "cnpjPrestador": "null"
}

# URL base para envio do formulário
url_formulario = "http://visualizar.ginfes.com.br/report/exportacao"

# Diretório para salvar o PDF
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

try:
    # Realiza a consulta inicial
    response = session.get(url_consulta, params=params, verify=certifi.where())
    response.raise_for_status()  # Levanta exceção em caso de erro HTTP

    # Analisa o HTML usando lxml
    tree = html.fromstring(response.content)

    # Encontra o formulário com o nome 'exportar'
    form = tree.xpath("//form[@name='exportar']")
    if not form:
        print("Formulário 'exportar' não encontrado.")
        exit()

    # Coleta os campos do formulário
    form_data = {}
    inputs = form[0].xpath(".//input")
    for input_tag in inputs:
        name = input_tag.attrib.get('name')
        value = input_tag.attrib.get('value', '')
        form_data[name] = value

    # Altera os campos especificados
    form_data['imprime'] = '0'
    form_data['tipo'] = 'pdf'

    # Envia o POST com os dados alterados
    response = session.post(url_formulario, data=form_data, stream=True)
    response.raise_for_status()  # Levanta exceção em caso de erro HTTP

    # Verifica se o conteúdo é um PDF
    content_type = response.headers.get('Content-Type')
    if 'application/pdf' not in content_type:
        print("O retorno não é um arquivo PDF.")
        exit()

    # Salva o PDF no disco
    output_path = os.path.join(output_dir, f"nota_{params['numNota']}.pdf")
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"PDF salvo em: {output_path}")

except requests.exceptions.SSLError as e:
    print(f"Erro SSL: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
