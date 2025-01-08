from pytrustnfe.certificado import Certificado
from pytrustnfe.nfse.ginfes import consultar_situacao_lote

certificado = open("/Users/addo/jobs/addodelgrossi/go-nfs-e/resources/35143637000111.pfx", "rb").read()
certificado = Certificado(certificado, b'k4ex2018')

# Código de situação de lote de RPS
# 1 – Não Recebido
# 2 – Não Processado
# 3 – Processado com Erro
# 4 – Processado com Sucesso

obj = {'cnpj_prestador': '35143637000111', 'inscricao_municipal': '1366453', 'protocolo': '589918266'}
resposta = consultar_situacao_lote(certificado, consulta=obj, ambiente='producao')
# print(resposta)
# print(resposta['sent_xml'])
print(resposta['received_xml'])



# Acesse o site de seu município ([prefeitura].ginfes.com.br)
# Servidor de Produção: https://producao.ginfes.com.br/ServiceGinfesImpl?wsdl
# Servidor de Homologação: https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl
#
# Acesso as notas emitidas no hambiente de homolocação:
# http://municipio.ginfesh.com.br/
#
# +11 2175-1145 Atendimento Ginfes
# atendimento@ginfes.com.br (Todo o suporte deve ser feito por e-mail);
#
#
# Consulta situação lote RPS
# Situação do lote RPS
# 1 – Não Recebido
# 2 – Não Processado
# 3 – Processado com Erro
# 4 – Processado com Sucesso
