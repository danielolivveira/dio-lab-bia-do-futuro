# Código da Aplicação

Esta pasta contém o código do agente financeiro Finn.

## Estrutura

src/
└── app.py  # Aplicação principal com interface Streamlit e integração com Ollama

## Setup do Ollama

```
# 1. Instalar Ollama (ollama.com)
# 2. Baixar o modelo
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```
