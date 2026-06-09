# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento compatível com perfil moderado |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00 baseado no `transacoes.csv`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com perfil moderado (ex: Tesouro Selic ou FII)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual criptomoeda devo comprar?"
- **Resposta esperada:** Agente informa que não tem dados sobre criptomoedas
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Formulário de Feedback

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "A resposta respondeu sua pergunta?" | 4 |
| Segurança | "As informações pareceram confiáveis?" | 5 |
| Coerência | "A linguagem foi clara e fácil de entender?" | 4 |

**Comentário aberto:** O que poderia melhorar?
- As respostas às vezes são longas demais para perguntas simples.

---

## Resultados

**O que funcionou bem:**
- O Finn respondeu corretamente perguntas baseadas nos dados do `transacoes.csv`
- Recusou recomendar criptomoedas e produtos fora da base de conhecimento
- Manteve coerência com o perfil moderado do cliente em todas as sugestões

**O que pode melhorar:**
- O tempo de resposta é alto devido ao processamento local com Ollama
- Respostas muito longas em perguntas simples — o prompt poderia ser mais restritivo
- Em alguns casos repetiu informações do contexto desnecessariamente

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento.
