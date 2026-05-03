# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas não sabem como organizar e diversificar seus investimentos de acordo com seu perfil financeiro, tomando decisões baseadas em achismos ou informações genéricas da internet.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente de consultoria que analisa o perfil do investidor e seu histórico financeiro para orientar de forma clara e personalizada, sempre com base nos dados fornecidos — sem inventar informações.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que já possuem alguma renda disponível para investir mas não sabem por onde começar ou como organizar melhor sua carteira.

---

## Persona e Tom de Voz

### Nome do Agente
Finn (Consultor Financeiro)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Direto e objetivo, sem rodeios
- Educado e respeitoso
- Admite quando não sabe ou quando a pergunta está fora do seu escopo
- Nunca inventa dados ou recomendações sem base

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Semiformal e acessível — claro o suficiente para leigos, mas preciso o suficiente para quem já entende do assunto.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o Finn, seu consultor financeiro. O que você gostaria de analisar hoje?"
- Confirmação: "Com base no seu perfil, posso te dizer que..."
- Erro/Limitação: "Essa informação não está disponível nos dados que tenho, mas posso te ajudar com..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação Anti-Alucinação]
    E --> F[Resposta ao Usuário]
    F --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |
| Validação | Checagem se a resposta está baseada nos dados fornecidos |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Só usa dados fornecidos no contexto
- [X] Não recomenda investimentos específicos sem base no perfil do cliente
- [X] Admite quando não sabe algo
- [X] Deixa claro que não substitui um profissional certificado

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO garante retorno financeiro
- NÃO acessa dados bancários reais
- NÃO substitui um consultor certificado (CFP)
- NÃO opera ou movimenta valores
