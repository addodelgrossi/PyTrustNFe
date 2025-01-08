from pytrustnfe.certificado import Certificado
from pytrustnfe.nfse.ginfes import consultar_nfse

certificado = open("/Users/addo/jobs/addodelgrossi/go-nfs-e/resources/35143637000111.pfx", "rb").read()
certificado = Certificado(certificado, b'k4ex2018')

# Cnpj="35143637000111",
# InscricaoMunicipal="1366453"


# obj = {'cnpj_prestador': '35143637000111', 'inscricao_municipal': '1366453', 'data_inicial': '2024-12-01', 'data_final': '2024-12-31'}
obj = {'cnpj_prestador': '35143637000111', 'inscricao_municipal': '1366453', 'numero_nfse': '2325'}
# resposta = consultar_nfse(certificado, consulta=obj, ambiente='producao')
resposta = consultar_nfse(certificado, consulta=obj, ambiente='producao')
# print(resposta)
print(resposta['received_xml'])


# consultar_nfse(certificado, '35143637000111)
# https://github.com/danimaribeiro/PyTrustNFe/issues/332
# https://github.com/addodelgrossi/PyTrustNFe
# https://github.com/willkerms/NFSe/blob/master/ginfes/NFSeGinfes.php

# https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-servico-v1/#/ServiceInvoices/ServiceInvoices_Post
