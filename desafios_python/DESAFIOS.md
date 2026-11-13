# 🥋 Bateria de Desafios Integrados: Python Puro para Dados & ML

> **Regra de Ouro:** Proibido usar bibliotecas externas (`pandas`, `numpy`, etc.). Todo o processamento deve ser feito com a biblioteca padrão do Python (`pure python`). O objetivo é forçar seu cérebro a pensar na arquitetura de dados, controle de fluxo e robustez de código.

---

## 🗺️ Mapa Conceitual Integrado

Em projetos reais de Engenharia de Dados e Machine Learning, os conceitos nunca aparecem isolados. Eles trabalham em cadeia:

```
[Dados Brutos Sujos (Strings)]
         │
         ▼  (try / except + métodos de string)
[Validação & Limpeza em Funções (def)]
         │
         ▼  (list comprehensions + tuplas imutáveis)
[Estruturação em Memória (Listas / Dicionários)]
         │
         ▼  (sets para unicidade + loops com acumuladores)
[Deduplicação, Agregação & Métricas]
```

---

## 🥊 Nível 1: O Sanitizador Defensivo de Leads (Fintech)
**Conceitos testados:** `def`, tipos primitivos, coerção segura, `try/except`, métodos de `str` (`strip`, `replace`, `lower`, `split`), condicionais e retorno padronizado (`dict` ou `tuple`).

### Contexto
Uma fintech capturou leads de clientes interessados em empréstimos. Os dados vieram de formulários web sem validação no front-end. O time de modelagem de crédito precisa que esses dados sejam limpos e padronizados antes de alimentar o modelo de Machine Learning.

### Dados de Entrada
Crie um arquivo `desafio_01.py` e use esta lista como entrada:

```python
leads_brutos = [
    "  101 ; ANA SILVA ; 29 ; R$ 4.500,00 ; SP ; aprovado ",
    "102;CARLOS SOUZA;trinta e dois;R$ 8.900,50;RJ;aprovado",
    " 103 ; beatriz lima ; 24 ; ; MG ; reprovado ",
    "104; DANIEL ALVES ; 41 ; R$ 12.000,00 ; sp ; APROVADO",
    "105;EDUARDO RAMOS;17;R$ 1.500,00;BA;reprovado",
    " ; Marcos Castro ; 35 ; R$ 3.200,00 ; GO ; pendente ",
    "107; Fernanda Torres ; 52 ; R$ -500,00 ; PR ; aprovado ",
    "108; Roberto Carlos ; 65 ; R$ 25.000,00 ; SP ; aprovado ",
]
```

### O que o seu código deve fazer:
Construa uma função principal `processar_lead(registro_str)` que receba uma linha de texto e retorne um dicionário limpo ou `None` caso o registro seja irrecuperável.

**Regras de Negócio e Validações:**
1. **ID:** Deve ser convertido para `int`. Se o ID estiver vazio ou não for número, o registro deve ser descartado.
2. **Nome:** Deve ficar com a primeira letra de cada palavra maiúscula (`.title()`) e sem espaços nas bordas.
3. **Idade:** Deve ser convertida para `int`. Se for menor de 18 anos ou se não for um número válido (ex: `"trinta e dois"`), o lead deve ser marcado como inválido/descartado.
4. **Renda:** Deve ser convertida para `float`. Se o campo estiver vazio, com valor negativo ou texto corrompido, tratar com `try/except` e descartar o lead.
5. **Estado (UF):** Deve ficar sempre em letras maiúsculas (`SP`, `RJ`, etc.).
6. **Status:** Padronizar para minúsculo (`aprovado`, `reprovado`, `pendente`).

### Saída Esperada no Terminal:
- Lista contendo apenas os dicionários dos **leads válidos**.
- Relatório no final:
  - Quantidade total de leads recebidos.
  - Quantidade de leads aprovados para a base de modelagem.
  - Quantidade de leads descartados por inconsistência.

---

## 🥊 Nível 2: Reconciliação Financeira e Anti-Fraude (Deduplicação & Agrupamento)
**Conceitos testados:** `set`, tuplas (como chaves de unicidade), `dict` como acumulador multidimensional, `for`, `in`, filtros lógicos.

### Contexto
O gateway de pagamento sofreu instabilidade de rede e algumas transações foram reenviadas múltiplas vezes (duplicadas com mesmo cliente, valor e timestamp). Além disso, clientes que realizaram transações acima de R$ 10.000,00 em horários noturnos (fora da faixa das 06:00 às 22:00) devem cair na esteira de auditoria de risco.

### Dados de Entrada
Crie um arquivo `desafio_02.py` e use esta base:

```python
logs_transacoes = [
    {"id": "tx1", "cliente": "Ryan", "valor": 12500.0, "hora": 23, "cidade": "Goiânia"},
    {"id": "tx2", "cliente": "Lucas", "valor": 300.0, "hora": 14, "cidade": "São Paulo"},
    {"id": "tx3", "cliente": "Ryan", "valor": 12500.0, "hora": 23, "cidade": "Goiânia"},  # Duplicada
    {"id": "tx4", "cliente": "Carla", "valor": 8000.0, "hora": 9, "cidade": "Brasília"},
    {"id": "tx5", "cliente": "Lucas", "valor": 300.0, "hora": 14, "cidade": "São Paulo"},  # Duplicada
    {"id": "tx6", "cliente": "Beatriz", "valor": 15000.0, "hora": 2, "cidade": "Goiânia"},
    {"id": "tx7", "cliente": "Ryan", "valor": 450.0, "hora": 15, "cidade": "Goiânia"},
    {"id": "tx8", "cliente": "Marcos", "valor": 22000.0, "hora": 21, "cidade": "Anápolis"},
]
```

### O que o seu código deve fazer:
1. **Deduplicação Inteligente com `set`:**
   - Duas transações são consideradas a mesma se tiverem **o mesmo cliente, mesmo valor e mesma hora**.
   - Use um `set` de tuplas para filtrar e manter apenas transações únicas em uma lista chamada `transacoes_unicas`.
2. **Esteira de Fraude Noturna:**
   - Em um único laço, identifique transações onde: `valor > 10000.0` E (`hora >= 22` OU `hora < 6`).
   - Salve os alertas em uma lista de tuplas contendo `(cliente, valor, cidade)`.
3. **Agrupamento por Cidade:**
   - Calcule o volume financeiro total transacionado (apenas das transações únicas) para cada cidade usando um dicionário acumulador.

### Saída Esperada no Terminal:
- Total de transações processadas vs Total de transações deduplicadas.
- Lista de alertas de fraude noturna.
- Dicionário com faturamento total consolidado por cidade.

---

## 🥊 Nível 3: O Mini-Motor de Métricas de Machine Learning (Funções & Redução Matemática)
**Conceitos testados:** `def`, `zip` ou `range(len())`, list comprehension com validação, cálculo de métricas na mão (Sem Scikit-Learn!), operações matemáticas com acumulador.

### Contexto
Você treinou seu primeiro modelo de regressão para prever o preço de carros usados (preparando o terreno para o projeto da Fenabrave). O modelo gerou previsões, mas o log de predição gravou alguns valores corrompidos (`None`, textos vazios). Você precisa limpar os pares (Real vs Previsto) e calcular na mão o **MAE (Mean Absolute Error - Erro Médio Absoluto)** e o **RMSE (Root Mean Squared Error - Raiz do Erro Quadrático Médio)**.

### Fórmulas Matemáticas:
- **Erro Absoluto:** $|Real - Previsto|$ (em Python: `abs(real - previsto)`)
- **MAE:** Média de todos os erros absolutos.
- **Erro Quadrático:** $(Real - Previsto)^2$ (em Python: `(real - previsto) ** 2`)
- **RMSE:** Raiz quadrada da média dos erros quadráticos (em Python: `media_quadratica ** 0.5`)

### Dados de Entrada
Crie um arquivo `desafio_03.py`:

```python
precos_reais = [45000.0, 72000.0, "corrompido", 110000.0, 28000.0, 65000.0, ""]
precos_previstos = [43500.0, 75000.0, 80000.0, 102000.0, "erro", 64500.0, 30000.0]
```

### O que o seu código deve fazer:
1. Criar uma função `alinhar_e_limpar_predicoes(reais, previstos)`:
   - Os dois vetores têm que ter o mesmo tamanho.
   - Deve ignorar qualquer par onde o valor real OU o previsto não consiga ser convertido para `float` com segurança (`try/except`).
   - Retornar duas listas limpas de floats com exatamente os mesmos índices válidos.
2. Criar uma função `calcular_mae(y_real, y_pred)`:
   - Retorna o Erro Médio Absoluto formatado em R$.
3. Criar uma função `calcular_rmse(y_real, y_pred)`:
   - Retorna o RMSE formatado em R$.
4. Identificar o caso com o **Maior Erro Individual** (mostrar qual foi o valor real, previsto e a diferença).

---

## 🥊 Nível 4 (O Chefão): Pipeline de Ingestão de Log de Acessos (Streaming em Lote)
**Conceitos testados:** Todos os anteriores combinados + contadores de frequência + lógica de detecção de ataque de força bruta.

### Contexto
O servidor da sua aplicação gerou um arquivo de log textual bruto com requisições. O seu script deve ler a lista bruta de linhas, extrair os dados, auditar requisições inválidas e detectar possíveis ataques de força bruta (IPs com muitos erros 401/403).

### Dados de Entrada
Crie um arquivo `desafio_04.py`:

```python
logs_servidor = [
    "2026-10-28 01:00:10 | 192.168.1.10 | GET /home | 200 | 120ms",
    "2026-10-28 01:00:12 | 192.168.1.15 | POST /login | 401 | 45ms",
    "2026-10-28 01:00:13 | 192.168.1.15 | POST /login | 401 | 50ms",
    "2026-10-28 01:00:14 | 192.168.1.15 | POST /login | 401 | 48ms",
    "2026-10-28 01:00:15 | 192.168.1.20 | GET /dashboard | 200 | 310ms",
    "linha_corrompida_sem_separadores",
    "2026-10-28 01:00:18 | 192.168.1.15 | POST /login | 401 | 40ms",
    "2026-10-28 01:00:20 | 192.168.1.25 | GET /produtos | 404 | 15ms",
    "2026-10-28 01:00:22 | 192.168.1.10 | GET /perfil | 200 | 180ms",
    "2026-10-28 01:00:25 | 192.168.1.15 | POST /login | 200 | 95ms",
]
```

### O que o seu código deve fazer:
1. **Parser de Log:**
   - Criar uma função `fazer_parse_linha(linha)` que divide a string por `"|"` e remove os espaços das bordas.
   - Extrair: `timestamp`, `ip`, `metodo_rota`, `status_code` (como `int`), `tempo_ms` (como `int`, extraindo o número antes de `"ms"`).
   - Se a linha não tiver os 5 elementos ou o status/tempo falharem na conversão, tratar defensivamente com `try/except` e ignorar.
2. **Estatísticas de Tráfego:**
   - Contar total de requisições por código de status (`200`, `401`, `404`) usando dicionário.
   - Calcular o tempo médio de resposta das requisições bem-sucedidas (`status == 200`).
3. **Detector de Força Bruta (Auditoria de Segurança):**
   - Descobrir quais IPs tiveram **3 ou mais falhas de autenticação (`status == 401`)**.
   - Imprimir o alerta com o IP do agressor e a quantidade de tentativas bloqueadas.

---

## 🚀 Como Executar o Treino
1. Crie os arquivos dentro da pasta `desafios_python/` (ex: `desafio_01.py`, `desafio_02.py`, etc.).
2. Escreva o código do seu jeito, pensando na estrutura e no porquê de cada linha.
3. Execute no terminal:
   ```powershell
   python .\desafios_python\desafio_01.py
   ```
4. Quando rodar ou se travar em alguma lógica, me avise para analisarmos a fundo o código juntos, linha por linha!
