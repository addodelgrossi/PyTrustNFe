from pytrustnfe.certificado import Certificado
from pytrustnfe.nfse.ginfes import recepcionar_lote_rps

certificado = open("/Users/addo/jobs/addodelgrossi/go-nfs-e/resources/35143637000111.pfx", "rb").read()
certificado = Certificado(certificado, b'k4ex2018')

# Cnpj="35143637000111",
# InscricaoMunicipal="1366453"

obj = {
    'numero_lote': '20250102',
    'cnpj_prestador': '35143637000111',
    'inscricao_municipal': '1366453',
    'lista_rps': [
        {
            'numero': '5',
            'serie': '1',
            'tipo_rps': '1',
            'data_emissao': '2025-01-02T14:25:00',
            'natureza_operacao': '1',
            'regime_tributacao': '6',
            'optante_simples': '1',
            'incentivador_cultural': '2',
            'status': '1',
            # 'numero_substituido': '0',
            # 'serie_substituido': '0',
            # 'tipo_substituido': '0',
            'prestador': {
                'cnpj': '35143637000111',
                'inscricao_municipal': '1366453',
            },
            'tomador': {
                'cnpj_cpf': '33308424000177',
                'razao_social': 'ECHOPE 01 LTDA',
                'logradouro': 'RUA 9 DE JULHO',
                'numero': '2117',
                # 'complemento': '',
                'bairro': 'CENTRO',
                'cidade': '3550308',
                'uf': 'SP',
                'cep': '14801295',
                'telefone': '1633977000',
                'email': 'araraquara01@echope.com.br'
            },
            'valor_servico': '10.00',
            # 'valor_deducao': '0.00',
            # 'valor_pis': '0.00',
            # 'valor_cofins': '0.00',
            # 'valor_inss': '0.00',
            # 'valor_ir': '0.00',
            # 'valor_csll': '0.00',
            'iss_retido': '2',
            # 'valor_iss': '0.00',
            # 'valor_iss_retido': '0.00',
            # 'outras_retencoes': '0.00',
            'base_calculo': '10.00',
            'aliquota_issqn': '0.0353',
            'valor_liquido_nfse': '10.00',
            # 'desconto_incondicionado': '0.00',
            # 'desconto_condicionado': '0.00',
            'codigo_servico': '107', # sem pontuacao
            # 'cnae_servico': '6209100',
            # 'codigo_tributacao_municipio': '1.07/6209100',
            # 'codigo_tributacao_municipio': '107:6209100',
            'codigo_tributacao_municipio': '6209100',
            'descricao': 'Teste de RPS',
            'codigo_municipio': '3503208',
        },
    ]
}

# <Rps>
#     <InfRps Id="rps{{ rps.numero }}">
#         <IdentificacaoRps>
#             <Numero>{{ rps.numero }}</Numero>
#             <Serie>{{ rps.serie }}</Serie>
#             <Tipo>{{ rps.tipo_rps }}</Tipo>
#         </IdentificacaoRps>
#         <DataEmissao>{{ rps.data_emissao }}</DataEmissao>
#         <NaturezaOperacao>{{ rps.natureza_operacao }}</NaturezaOperacao>
#         <RegimeEspecialTributacao>{{ rps.regime_tributacao }}</RegimeEspecialTributacao>
#         <OptanteSimplesNacional>{{ rps.optante_simples }}</OptanteSimplesNacional>
#         <IncentivadorCultural>{{ rps.incentivador_cultural }}</IncentivadorCultural>
#         <Status>{{ rps.status }}</Status>
#         <RpsSubstituido>
#             <Numero>{{ rps.numero_substituido }}</Numero>
#             <Serie>{{ rps.serie_substituido }}</Serie>
#             <Tipo>{{ rps.tipo_substituido }}</Tipo>
#         </RpsSubstituido>
#         <Servico>
#             <Valores>
#                 <ValorServicos>{{ rps.valor_servico }}</ValorServicos>
#                 <ValorDeducoes>{{ rps.valor_deducao }}</ValorDeducoes>
#                 <ValorPis>{{ rps.valor_pis }}</ValorPis>
#                 <ValorCofins>{{ rps.valor_cofins }}</ValorCofins>
#                 <ValorInss>{{ rps.valor_inss }}</ValorInss>
#                 <ValorIr>{{ rps.valor_ir }}</ValorIr>
#                 <ValorCsll>{{ rps.valor_csll }}</ValorCsll>
#                 <IssRetido>{{ rps.iss_retido }}</IssRetido>
#                 <ValorIss>{{ rps.valor_iss }}</ValorIss>
#                 <ValorIssRetido>{{ rps.valor_iss_retido }}</ValorIssRetido>
#                 <OutrasRetencoes>{{ rps.outras_retencoes }}</OutrasRetencoes>
#                 <BaseCalculo>{{ rps.base_calculo }}</BaseCalculo>
#                 <Aliquota>{{ rps.aliquota_issqn }}</Aliquota>
#                 <ValorLiquidoNfse>{{ rps.valor_liquido_nfse }}</ValorLiquidoNfse>
#                 <DescontoIncondicionado>{{ rps.desconto_incondicionado }}</DescontoIncondicionado>
#                 <DescontoCondicionado>{{ rps.desconto_condicionado }}</DescontoCondicionado>
#             </Valores>
#             <ItemListaServico>{{ rps.codigo_servico }}</ItemListaServico>
#             <CodigoCnae>{{ rps.cnae_servico }}</CodigoCnae>
#             <CodigoTributacaoMunicipio>{{ rps.codigo_tributacao_municipio }}</CodigoTributacaoMunicipio>
#             <Discriminacao>{{ rps.descricao }}</Discriminacao>
#             <CodigoMunicipio>{{ rps.codigo_municipio }}</CodigoMunicipio>
#         </Servico>
#         <Prestador>
#             <Cnpj>{{ rps.prestador.cnpj }}</Cnpj>
#             <InscricaoMunicipal>{{ rps.prestador.inscricao_municipal }}</InscricaoMunicipal>
#         </Prestador>
#         <Tomador>
#             <IdentificacaoTomador>
#                 <CpfCnpj>
#                     {% if rps.tomador.cnpj_cpf|length == 14  %}
#                     <Cnpj>{{ rps.tomador.cnpj_cpf }}</Cnpj>
#                     {% endif %}
#                     {% if rps.tomador.cnpj_cpf|length == 11  %}
#                     <Cpf>{{ rps.tomador.cnpj_cpf }}</Cpf>
#                     {% endif %}
#                 </CpfCnpj>
#                 <InscricaoMunicipal>{{ rps.tomador.inscricao_municipal }}</InscricaoMunicipal>
#             </IdentificacaoTomador>
#             <RazaoSocial>{{ rps.tomador.razao_social }}</RazaoSocial>
#             <Endereco>
#                 <Endereco>{{ rps.tomador.logradouro }}</Endereco>
#                 <Numero>{{ rps.tomador.numero }}</Numero>
#                 <Complemento>{{ rps.tomador.complemento }}</Complemento>
#                 <Bairro>{{ rps.tomador.bairro }}</Bairro>
#                 <CodigoMunicipio>{{ rps.tomador.cidade }}</CodigoMunicipio>
#                 <Uf>{{ rps.tomador.uf }}</Uf>
#                 <Cep>{{ rps.tomador.cep }}</Cep>
#             </Endereco>
#             <Contato>
#                 <Telefone>{{ rps.tomador.telefone }}</Telefone>
#                 <Email>{{ rps.tomador.email }}</Email>
#             </Contato>
#         </Tomador>
#         {% if rps.intermediario is defined -%}
#         <IntermediarioServico>
#             <RazaoSocial>{{ rps.intermediario.razao_social }}</RazaoSocial>
#             <CpfCnpj>
#                 <Cnpj>{{ rps.intermediario.cnpj }}</Cnpj>
#             </CpfCnpj>
#             <InscricaoMunicipal>{{ rps.intermediario.inscricao_municipal }}</InscricaoMunicipal>
#         </IntermediarioServico>
#         {% endif %}
#         {% if rps.construcao_civil is defined -%}
#         <ContrucaoCivil>
#             <CodigoObra>{{ rps.construcao_civil.codigo_obra }}</CodigoObra>
#             <Art>{{ rps.construcao_civil.art }}</Art>
#         </ContrucaoCivil>
#         {% endif %}
#     </InfRps>
# </Rps>


# obj = {'cnpj_prestador': '35143637000111', 'inscricao_municipal': '1366453', 'data_inicial': '2024-12-01', 'data_final': '2024-12-31'}
# resposta = consultar_nfse(certificado, consulta=obj, ambiente='producao')
resposta = recepcionar_lote_rps(certificado, nfse=obj, ambiente='producao')
print(resposta)

# create file from response
with open("response.xml", "w") as f:
    f.write(resposta['received_xml'])

with open("lote.xml", "w") as f:
    f.write(resposta['sent_xml'])

# consultar_nfse(certificado, '35143637000111)
# https://github.com/danimaribeiro/PyTrustNFe/issues/332
# https://github.com/addodelgrossi/PyTrustNFe
# https://github.com/willkerms/NFSe/blob/master/ginfes/NFSeGinfes.php

# https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-servico-v1/#/ServiceInvoices/ServiceInvoices_Post
