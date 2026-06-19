from openai import OpenAI

client = OpenAI(
    api_key="SUA_API_KEY"
)

cliente = {
    "empresa": "Alpha Tecnologia",
    "segmento": "Software",
    "dias_sem_contato": 120,
    "interesse": "Alto",
    "numero_reunioes": 3,
    "valor_potencial": "R$ 50.000"
}

prompt = f"""
Você é um consultor especialista em CRM e inteligência comercial.

Analise os dados fornecidos e gere:

1. Resumo executivo
2. Oportunidades identificadas
3. Possíveis riscos
4. Prioridade comercial
5. Próximas ações recomendadas

Dados:

Empresa: {cliente['empresa']}
Segmento: {cliente['segmento']}
Dias sem contato: {cliente['dias_sem_contato']}
Interesse: {cliente['interesse']}
Número de reuniões: {cliente['numero_reunioes']}
Valor potencial: {cliente['valor_potencial']}
"""

resposta = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em inteligência comercial."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(resposta.choices[0].message.content)
