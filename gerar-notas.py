import pandas as pd
import json

from datetime import datetime
from pytrustnfe.certificado import Certificado
from pytrustnfe.nfse.ginfes import recepcionar_lote_rps

certificado = open("/Users/addo/jobs/addodelgrossi/go-nfs-e/resources/35143637000111.pfx", "rb").read()
certificado = Certificado(certificado, b'k4ex2018')


filename = '/Users/addo/Downloads/teste_emissao_nf.xlsx'
df = pd.read_excel(filename, skiprows=1)

lista_rps = []
serie = '3'
for index, row in df.iterrows():
    item = {
        'numero': str(index + 1),  # Número sequencial (começa em 1)
        'serie': serie,
        'tipo_rps': '1',
        # 'data_emissao': '2025-01-02T14:25:00',
        'data_emissao': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'natureza_operacao': '1',
        'regime_tributacao': '6',
        'optante_simples': '1',
        'incentivador_cultural': '2',
        'status': '1',
        'prestador': {
            'cnpj': str(row['CNPJ']),
            'inscricao_municipal': str(row['INSCRICAO']),
        },
        'tomador': {
            'cnpj_cpf': str(row['CLIENTE_CNPJ']),  # CNPJ
            'razao_social': row['RAZAO SOCIAL'],  # Razão social
            'logradouro': row['LOGRADOURO'],  # Logradouro
            'numero': str(row['NUMERO']),  # Número
            'bairro': row['BAIRRO'],  # Bairro
            'cidade': row['CIDADE'],  # Cidade
            'uf': row['UF'],  # UF
            'cep': str(row['CEP']).replace('-', ''),  # CEP sem pontuação
            'telefone': str(row['TELEFONE']),  # Telefone
            'email': row['EMAIL'],  # E-mail
        },
        'valor_servico': f"{row['VALOR_SERVICO']:.2f}",  # Valor do serviço
        'iss_retido': '2',
        'base_calculo': f"{row['VALOR_SERVICO']:.2f}",  # Base de cálculo
        'aliquota_issqn': f"{(row['ALIQUOTA_ISSQN']/100):.4f}",  # Alíquota
        'valor_liquido_nfse': f"{row['VALOR_SERVICO']:.2f}",  # Valor líquido
        'codigo_servico': str(row['CODIGO_SERVICO']),  # Código do serviço
        'codigo_tributacao_municipio': str(row['CODIGO_TRIBUTACAO_MUNICIPIO']),  # Código de tributação
        'descricao': row['DESCRICAO'],  # Descrição
        'codigo_municipio': '3503208',  # Código do município fixo
    }
    lista_rps.append(item)

# resultado = {'lista_rps': lista_rps}

obj = {
    'numero_lote': datetime.now().strftime('%Y%m%d%H%M%S'),
    'cnpj_prestador': '35143637000111',
    'inscricao_municipal': '1366453',
    'lista_rps': lista_rps
}

print(json.dumps(obj, indent=4, ensure_ascii=False))

resposta = recepcionar_lote_rps(certificado, nfse=obj, ambiente='producao')
print(resposta)

# create file from response
with open("response.xml", "w") as f:
    f.write(resposta['received_xml'])

with open("lote.xml", "w") as f:
    f.write(resposta['sent_xml'])



# # Opcional: Salvar em um arquivo JSON
# with open('resultado_rps.json', 'w', encoding='utf-8') as f:
#     json.dump(resultado, f, indent=4, ensure_ascii=False)
