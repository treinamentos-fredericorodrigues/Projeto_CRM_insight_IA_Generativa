"""
============================================================
CRM INSIGHT AI
============================================================

Projeto Educacional de Inteligência Artificial Generativa
aplicada à análise de CRM e apoio à tomada de decisão.

Autor:
Frederico Rodrigues de Oliveira

Objetivo:
Demonstrar, durante as aulas, como a Inteligência Artificial
Generativa pode ser utilizada para analisar informações
comerciais e gerar recomendações estratégicas para vendedores
e gestores.

Tecnologias:
- Python
- OpenAI GPT-4o
- Engenharia de Prompt
- Inteligência Artificial Generativa
============================================================
"""

# ==========================================================
# IMPORTAÇÃO DA BIBLIOTECA OPENAI
# ==========================================================
# Necessária para realizar a comunicação com o modelo GPT.
# Instalação, digite na primeira célula o seguinte código:
# 
!pip install -q openai

#
# ==========================================================

from openai import OpenAI


# ==========================================================
# CONFIGURAÇÃO DA API
# ==========================================================
# Substitua "SUA_API_KEY" pela sua chave da OpenAI
# quando for executar localmente ou no Google Colab.
#
# IMPORTANTE:
# Não publique sua chave real no GitHub.
# ==========================================================

client = OpenAI(
    api_key="SUA_API_KEY"
)

# ==========================================================
# DADOS DO CLIENTE
# ==========================================================
# Essas informações simulam dados obtidos de um CRM.
#
# Em um projeto real:
# - Salesforce
# - Dynamics 365
# - HubSpot
# - Pipedrive
#
# Os dados poderiam ser importados automaticamente.
# ==========================================================

cliente = {
    "empresa": "Alpha Tecnologia",
    "segmento": "Software",
    "dias_sem_contato": 120,
    "interesse": "Alto",
    "numero_reunioes": 3,
    "valor_potencial": "R$ 50.000"
}

# ==========================================================
# PROMPT
# ==========================================================
# O prompt é a instrução enviada para a IA.
#
# Aqui estamos orientando o modelo para agir como um
# consultor comercial especializado em CRM.
# ==========================================================

prompt = f"""
Você é um consultor especialista em CRM e Inteligência Comercial.

Analise os dados fornecidos e gere:

1. Resumo executivo;
2. Oportunidades identificadas;
3. Possíveis riscos;
4. Prioridade comercial;
5. Próximas ações recomendadas.

Dados do cliente:

Empresa: {cliente['empresa']}
Segmento: {cliente['segmento']}
Dias sem contato: {cliente['dias_sem_contato']}
Interesse: {cliente['interesse']}
Número de reuniões: {cliente['numero_reunioes']}
Valor potencial: {cliente['valor_potencial']}

Utilize linguagem profissional e voltada para gestores.
"""

# ==========================================================
# CHAMADA DA IA GENERATIVA
# ==========================================================
# A instrução abaixo envia os dados para o modelo GPT.
#
# O modelo interpretará as informações e retornará
# uma análise completa.
# ==========================================================

resposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": """
            Você é um especialista em CRM,
            inteligência comercial,
            vendas consultivas e gestão de clientes.
            """
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

# ==========================================================
# EXIBIÇÃO DOS RESULTADOS
# ==========================================================
# A IA gera um relatório executivo contendo:
#
# - Resumo executivo
# - Oportunidades
# - Riscos
# - Prioridade comercial
# - Recomendações
# ==========================================================

print("\n")
print("=" * 70)
print("RELATÓRIO GERADO PELO CRM INSIGHT AI")
print("=" * 70)
print("\n")

print(resposta.choices[0].message.content)

print("\n")
print("=" * 70)
print("FIM DA ANÁLISE")
print("=" * 70)

# ==========================================================
# APLICAÇÃO EDUCACIONAL
# ==========================================================
#
# Este projeto foi desenvolvido para demonstrar,
# em ambiente de ensino, como a Inteligência
# Artificial Generativa pode ser aplicada
# em problemas reais de negócio.
#
# Durante as aulas os estudantes podem:
#
# ✅ Compreender o funcionamento de LLMs
#
# ✅ Estudar Engenharia de Prompt
#
# ✅ Explorar aplicações empresariais da IA
#
# ✅ Simular cenários de CRM
#
# ✅ Desenvolver pensamento analítico
#
# ✅ Apoiar a tomada de decisão baseada em dados
#
# ==========================================================
