# 🚀 Core Data & ML Engine: Algoritmos e Pipelines em Python Puro

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Performance](https://img.shields.io/badge/Complexity-O(n)%20Optimal-brightgreen?style=for-the-badge)](https://en.wikipedia.org/wiki/Time_complexity)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-success?style=for-the-badge)](https://peps.python.org/pep-0008/)

Pipeline de engenharia de dados, detecção de fraude, motor de validação de métricas de Machine Learning e auditoria de infraestrutura construído **do zero em Python puro**, sem dependência de bibliotecas externas (`pandas` ou `scikit-learn`), focando em alta performance de memória, tratamento cirúrgico de exceções e complexidade temporal $O(n)$.

---

## 1. Objetivo

No ecossistema de Engenharia de Dados e Machine Learning, a dependência cega de bibliotecas de alto nível frequentemente mascara gargalos de processamento, estouros de memória e comportamentos inesperados causados por dados corrompidos. 

Este projeto foi desenvolvido com quatro objetivos práticos de engenharia:
1. **Sanitização Resiliente de Dados (Fintech):** Ingestão de leads cadastrais com tratamento estrito de tipagem e isolamento de falhas via `try/except`.
2. **Reconciliação e Auditoria Anti-Fraude:** Deduplicação em tempo linear $O(n)$ utilizando tabelas hash (`set` e tuplas imutáveis) e acumuladores dinâmicos de faturamento por praça.
3. **Motor Matemático de Métricas de ML:** Avaliação manual de resíduos de regressão (MAE e RMSE) garantindo alinhamento de vetores e imunidade a anomalias de entrada.
4. **Parser de Logs & Detecção de Força Bruta:** Auditoria de tráfego de servidores, cálculo de latência de resposta e identificação proativa de tentativas de invasão (HTTP 401).

---

## 2. Demonstração

Abaixo estão os relatórios gerados no terminal após o processamento de cada módulo do pipeline:

### 🔹 Módulo 01: Sanitização de Leads
```text
=== RELATÓRIO FINAL DE LEADS ===
Total de leads recebidos: 8
Leads aprovados para base: 3
Leads descartados: 5
```

### 🔹 Módulo 02: Reconciliação Financeira & Anti-Fraude
```text
=== RELATÓRIO DE RECONCILIAÇÃO FINANCEIRA ===
Transações brutas recebidas : 8
Transações únicas válidas   : 6
Duplicadas descartadas      : 2
[ALERTAS DE FRAUDE NOTURNA]:
- Cliente: Ryan | Valor: R$ 12500.00 | Cidade: Goiânia
- Cliente: Beatriz | Valor: R$ 15000.00 | Cidade: Goiânia
[FATURAMENTO POR CIDADE]:
- Goiânia: R$ 12950.00
- São Paulo: R$ 300.00
- Brasília: R$ 8000.00
- Anápolis: R$ 22000.00
```

### 🔹 Módulo 03: Motor de Avaliação de Regressão (ML)
```text
=== AVALIAÇÃO DE DESEMPENHO DO MODELO ===
Total de predições recebidas : 7
Pares válidos analisados     : 5
Pares inválidos descartados  : 2
Erro Médio Absoluto (MAE)    : R$ 3250.00
Raiz do Erro Quadrático (RMSE): R$ 4344.54
Maior Erro Individual Identificado:
- Valor Real      : R$ 110000.00
- Valor Previsto  : R$ 102000.00
- Diferença Abs.  : R$ 8000.00
```

### 🔹 Módulo 04: Auditoria de Logs & Detecção de Ataque
```text
=== RELATÓRIO DE AUDITORIA DE LOGS ===
Total de requisições processadas: 7
Erros de parsing descartados     : 1
Distribuição de Status Code:
- 200: 4 requisições
- 500: 1 requisições
- 401: 4 requisições
Métricas de Performance:
- Tempo médio de resposta (Status 200): 176.25 ms
[ALERTA DE SEGURANÇA - FORÇA BRUTA]:
[ALERTA] IP: 192.168.1.50 com 3 tentativas consecutivas de falha de login!
```

---

## 3. Tecnologias Utilizadas

- **Linguagem:** Python 3.10+ (Built-in Standard Library)
- **Estruturas de Dados:** `set` (hashing para deduplicação instantânea), `tuple` (imutabilidade de chaves compostas), `dict` (acumuladores dinâmicos $O(1)$)
- **Controle de Fluxo & Tratamento de Erros:** `try / except` (`ValueError`, `TypeError`), `zip()`, desempacotamento de iteráveis (`.items()`)
- **Versionamento:** Git com Conventional Commits

---

## 4. Estrutura do Projeto

```text
.
├── desafios_python/
│   ├── desafio_01.py   # Sanitizador de leads com regras de negócio e tipagem
│   ├── desafio_02.py   # Reconciliação financeira, deduplicação O(n) e antifraude
│   ├── desafio_03.py   # Motor de métricas de ML puro (MAE, RMSE, resíduos)
│   ├── desafio_04.py   # Ingestão de logs de servidor e detecção de brute force
│   └── DESAFIOS.md     # Enunciados e requisitos de cada nível técnico
└── README.md           # Documentação técnica e benchmarks do projeto
```

---

## 5. Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado na máquina.
- Nenhuma biblioteca externa é necessária (zero dependências no pip).

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/ryanaurelio2005/python-pure-data-challenges.git
   cd python-pure-data-challenges
   ```

2. **Execute qualquer um dos módulos diretamente no terminal:**
   ```bash
   # Executar o sanitizador de leads:
   python desafios_python/desafio_01.py

   # Executar a reconciliação e antifraude:
   python desafios_python/desafio_02.py

   # Executar o motor de métricas de ML:
   python desafios_python/desafio_03.py

   # Executar a auditoria de logs e segurança:
   python desafios_python/desafio_04.py
   ```

---

## 6. Dataset

Os dados utilizados representam payloads reais de bancos transacionais, gateways de pagamento e servidores web, estruturados como fixtures de teste para validação de borda:

- **Leads Brutos:** Strings delimitadas por ponto e vírgula contendo ruído, campos nulos, valores monetários em formato brasileiro e idades por extenso.
- **Transações de Pagamento:** Payloads JSON simulando logs com duplicatas provocadas por instabilidade de rede e transações de alto valor em horários de risco.
- **Predições de Regressão:** Vetores pareados de valores reais versus previstos com strings corrompidas e valores vazios simulando falhas de log de inferência.
- **Logs de Servidor:** Linhas tabulares delimitadas por `|` contendo timestamp, IP, rota HTTP, status code e latência em milissegundos.

---

## 7. Resultados & Eficiência

- **Otimização de Complexidade:** A substituição de buscas lineares em listas aninhadas por conjuntos de tuplas hashables reduziu o custo de deduplicação de $O(n^2)$ para $O(n)$, viabilizando processamento de grandes lotes em milissegundos.
- **Tolerância a Falhas:** 100% dos dados corrompidos ou mal formatados foram isolados e descartados sem interrupção abrupta dos scripts (zero unhandled exceptions).
- **Fidelidade Matemática:** Implementação precisa das fórmulas de erro absoluto e quadrático, reproduzindo exatamente o comportamento das funções de perda (*loss functions*) utilizadas em frameworks de Machine Learning.

---

## 8. Próximas Versões

- [ ] Implementação de testes unitários automatizados com `pytest`.
- [ ] Exportação dos relatórios processados diretamente para formatos colunares (Parquet).
- [ ] Adição de tipagem estática com `typing` e validação com `mypy`.
- [ ] Empacotamento dos módulos como pacote reutilizável para pipelines de dados.

---

## 👨‍💻 Autor

Desenvolvido por **[Ryan Aurélio](https://github.com/ryanaurelio2005)**.  
*Estudante de Ciência de Dados e Inteligência Artificial (PUC Goiás) | Foco em Engenharia de Machine Learning.*
