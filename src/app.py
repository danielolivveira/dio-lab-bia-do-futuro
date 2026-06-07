import json
import pandas as pd
import requests
import streamlit as st

# =========== CONFIGURAÇÕES ============
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'gpt-oss'

# =========== CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =========== MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Finn, um consultor financeiro inteligente e direto.

OBJETIVO:
Orientar o usuário sobre investimentos e organização financeira com base
nos dados fornecidos, de forma clara, honesta e personalizada.

REGRAS:
1. Baseie suas respostas APENAS nos dados fornecidos no contexto;
2. Nunca invente rendimentos, taxas ou recomendações sem base nos dados; 
3. Se não souber algo, diga claramente: "Não tenho essa informação disponível";
4. Não recomende investimentos específicos sem considerar o perfil do usuário;
5. Lembre sempre que não substitui um consultor certificado (CFP);
6. Seja direto: vá ao ponto sem rodeios, mas mantenha o respeito.
"""

# =========== CHAMAR OLLAMA ============


def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={
                      "model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# ========== INTERFACE ==========
st.title("🎓 Finn, Seu Consultor Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
