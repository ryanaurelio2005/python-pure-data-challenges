# 🥋 Python Pure Data Challenges: Pre-OOP Foundation Track

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style: Clean](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen?style=for-the-badge)](https://peps.python.org/pep-0008/)

Série prática de desafios em **Python Puro** (*Pure Python* — sem Pandas ou NumPy), focada no desenvolvimento do raciocínio analítico, manipulação nativa de estruturas de dados e tratamento defensivo antes da transição para Programação Orientada a Objetos (POO).

---

## 1. Objetivo

Na preparação para atuar como Engenheiro de Machine Learning e Cientista de Dados, depender exclusivamente de bibliotecas de alto nível como Pandas sem dominar os fundamentos da linguagem cria lacunas severas de lógica, controle de exceções e compreensão da complexidade algorítmica ($O(1)$ vs $O(N)$).

Este repositório documenta a resolução prática de problemas reais de engenharia e análise de dados utilizando **estritamente os recursos nativos da biblioteca padrão do Python**:

- **Desafio 01 (Sanitizador de Leads de Fintech):** Tratamento defensivo de dados cadastrais textuais despadronizados vindos de formulários web, com coerção segura de tipos (`try...except ValueError`), filtros de elegibilidade e estruturação em dicionários.
- **Desafio 02 (Reconciliação Financeira & Anti-Fraude):** Deduplicação de transações em tempo constante ($O(1)$) através de chaves compostas em tuplas imutáveis e `set`, monitoramento em tempo real de transações noturnas de alto risco e consolidação de faturamento regional com acumuladores nativos em dicionários.

---

## 2. Demonstração

### Pipeline Nível 1: Sanitizador de Leads (`desafio_01.py`)

```mermaid
flowchart TD
    A["Leads Brutos (Lista de Strings)"] --> B["Split por ';' e remoção de espaços com strip()"]
    B --> C["Tratamento da Renda (.replace('R$', '').replace('.', '').replace(',', '.'))"]
    C --> D{"Coerção Numérica (try / except)"}
    D -- "ValueError (Ex: idade por extenso ou campo vazio)" --> E["Incrementa leads_descartados e pula (continue)"]
    D -- "Conversão bem-sucedida (int e float)" --> F{"Filtro de Negócio (idade < 18 ou valor <= 0)"}
    F -- "Sim (Menor de idade ou valor negativo/zero)" --> E
    F -- "Não (Lead elegível)" --> G["Criação do dicionário estruturado (title, upper, lower)"]
    G --> H["Adiciona na lista_clientes"]
    E --> I["Impressão do resultado e métricas no terminal"]
    H --> I
```

#### Saída no Terminal (`desafio_01.py`):
```text
[{'id': 101, 'nome': 'Ana Silva', 'idade': 29, 'valor': 4500.0, 'estado': 'SP', 'situacao': 'aprovado'}, {'id': 104, 'nome': 'Daniel Alves', 'idade': 41, 'valor': 12000.0, 'estado': 'SP', 'situacao': 'aprovado'}, {'id': 108, 'nome': 'Roberto Carlos', 'idade': 65, 'valor': 25000.0, 'estado': 'SP', 'situacao': 'aprovado'}]
Quantidades de leads recebidos: 8
Quantidade de leads aprovados: 3
Quantidade de leads descartados 5
```

---

### Pipeline Nível 2: Reconciliação & Anti-Fraude (`desafio_02.py`)

```mermaid
flowchart TD
    A["Logs de Transações Brutos (8 eventos)"] --> B["Iteração por registro"]
    B --> C["Gera tupla imutável de unicidade (cliente, valor, hora)"]
    C --> D{"Chave já presente no conjunto set?"}
    D -- "Sim (Transação Duplicada)" --> E["Incrementa transacoes_deduplicadas"]
    D -- "Não (Transação Nova/Única)" --> F["Registra chave no set e inclui na lista de transações únicas"]
    F --> G{"Filtro de Risco: valor > 10.000 e (hora >= 22 ou hora < 6)"}
    G -- "Sim (Suspeita Noturna)" --> H["Registra alerta (cliente, valor, cidade)"]
    G -- "Não (Transação Regular)" --> I["Prossegue para faturamento"]
    H --> I
    I --> J["Acumula volume financeiro da cidade no dicionário somatorio"]
    E --> K["Relatório de Reconciliação e Alertas no Terminal"]
    J --> K
```

#### Saída no Terminal (`desafio_02.py`):
```text
Transaçoes processadas: 6 | Transaçoes deduplicadas: 2
Lista de alertas de fraudes noturnos:
 [('Ryan', 12500.0, 'Goiânia'), ('Beatriz', 15000.0, 'Goiânia')]
Faturamento total consolidado por cidade:
{'Goiânia': 27950.0, 'São Paulo': 300.0, 'Brasília': 8000.0, 'Anápolis': 22000.0}
```

---

## 3. Tecnologias Utilizadas

- **Linguagem:** [Python 3.12](https://www.python.org/)
- **Estruturas de Dados Nativas & Complexidade:**
  - `set`: Busca e inserção de chaves em tempo constante médio ($O(1)$) via hashing, viabilizando deduplicação performática.
  - `tuple`: Estrutura imutável e hashable utilizada como chave composta para unicidade `(cliente, valor, hora)`.
  - `dict`: Mapeamento estruturado de entidades e acumulador de agregação por cidade.
  - `list`: Coleções sequenciais ordenadas de leads e transações.
- **Tratamento de Dados e Paradigma Procedimental:**
  - Encapsulamento de regras em funções reutilizáveis (`def processar_reconciliacao(...)`).
  - Métodos nativos de string (`strip`, `split`, `replace`, `title`, `upper`, `lower`).
  - Coerções primitivas seguras com `try...except ValueError`.
- **Versionamento:** [Git](https://git-scm.com/) e [GitHub](https://github.com/).

---

## 4. Estrutura do Projeto

```text
python-pure-data-challenges/
├── desafios/
│   ├── desafio_01.py        # Desafio 01: Sanitizador de Leads de Fintech
│   └── desafio_02.py        # Desafio 02: Reconciliação Financeira & Anti-Fraude Noturno
├── .gitignore               # Configuração para ignorar arquivos temporários e caches
├── README.md                # Documentação técnica completa do repositório
└── ROADMAP.md               # Guia com especificações e contexto dos próximos desafios
```

---

## 5. Como Executar

### Pré-requisitos
- Ter o **Python 3.10 ou superior** instalado na máquina.
- Git instalado (opcional, para clonar).

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/ryanaurelio2005/python-pure-data-challenges.git
   cd python-pure-data-challenges
   ```

2. **Executar o Desafio 01 (Sanitizador de Leads):**
   ```bash
   python .\desafios\desafio_01.py
   ```

3. **Executar o Desafio 02 (Reconciliação Financeira):**
   ```bash
   python .\desafios\desafio_02.py
   ```

*Nota: Não é necessária a instalação de nenhuma biblioteca externa (`pip`), pois todo o projeto foi construído utilizando apenas a biblioteca padrão do Python.*

---

## 6. Dataset

### Desafio 01: Lote de Leads Brutos (Strings)

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

| Campo | Posição | Tipo Esperado | Regra de Sanitização / Negócio |
| :--- | :---: | :---: | :--- |
| `id` | 0 | `int` | Conversão para inteiro. Descartado se vazio ou inválido. |
| `nome` | 1 | `str` | Remoção de espaços nas bordas e formatação em Title Case. |
| `idade` | 2 | `int` | Conversão para inteiro. Descartado se menor que 18 ou valor textual. |
| `renda` | 3 | `float` | Remoção de `"R$"`, pontuação monetária brasileira e descarte se $\le 0$. |
| `estado` | 4 | `str` | Padronização em maiúsculas (UF). |
| `situacao` | 5 | `str` | Padronização em minúsculas. |

---

### Desafio 02: Logs de Transações do Gateway (Dicionários)

```python
logs_transacoes = [
    {"id": "tx1", "cliente": "Ryan", "valor": 12500.0, "hora": 23, "cidade": "Goiânia"},
    {"id": "tx2", "cliente": "Lucas", "valor": 300.0, "hora": 14, "cidade": "São Paulo"},
    {"id": "tx3", "cliente": "Ryan", "valor": 12500.0, "hora": 23, "cidade": "Goiânia"},  # Duplicada de tx1
    {"id": "tx4", "cliente": "Carla", "valor": 8000.0, "hora": 9, "cidade": "Brasília"},
    {"id": "tx5", "cliente": "Lucas", "valor": 300.0, "hora": 14, "cidade": "São Paulo"},  # Duplicada de tx2
    {"id": "tx6", "cliente": "Beatriz", "valor": 15000.0, "hora": 2, "cidade": "Goiânia"},
    {"id": "tx7", "cliente": "Ryan", "valor": 450.0, "hora": 15, "cidade": "Goiânia"},
    {"id": "tx8", "cliente": "Marcos", "valor": 22000.0, "hora": 21, "cidade": "Anápolis"},
]
```

| Chave | Tipo | Descrição | Regra Aplicada |
| :--- | :---: | :--- | :--- |
| `id` | `str` | Identificador do evento no log | Rastreamento do evento no gateway. |
| `cliente` | `str` | Nome do cliente pagador | Parte da chave de unicidade. |
| `valor` | `float` | Valor transacionado em R$ | Gatilho de risco se $> 10.000,00$ e base do faturamento regional. |
| `hora` | `int` | Hora militar da transação (0-23) | Gatilho de risco noturno se $\ge 22$ ou $< 6$. |
| `cidade` | `str` | Praça de origem da operação | Dimensão de agregação do somatório de faturamento. |

---

## 7. Resultados

### Desafio 01 (Sanitização de Leads)
- **Total recebido:** 8 registros.
- **Aprovados:** 3 registros (37,5%) — Ana Silva, Daniel Alves e Roberto Carlos, em total conformidade cadastral e financeira.
- **Descartados:** 5 registros (62,5%) com inconsistências tratadas defensivamente (idade textual, renda vazia, menor de idade, ID em branco e renda negativa).

### Desafio 02 (Reconciliação Financeira & Anti-Fraude)
- **Volume total analisado:** 8 transações.
- **Deduplicação Inteligente:** 6 transações únicas mantidas e 2 transações duplicadas identificadas e descartadas (`tx3` de Ryan e `tx5` de Lucas).
- **Detecção de Fraude Noturna:** 2 transações de alto valor identificadas na faixa de risco:
  - `Ryan`: R$ 12.500,00 às 23h (Goiânia).
  - `Beatriz`: R$ 15.000,00 às 02h (Goiânia).
  - *Observação:* A transação do Marcos (R$ 22.000,00 em Anápolis) não gerou alerta por ocorrer às 21h (dentro do horário comercial padrão).
- **Faturamento Consolidado por Praça:**
  - **Goiânia:** R$ 27.950,00 (12.500 + 15.000 + 450)
  - **Anápolis:** R$ 22.000,00
  - **Brasília:** R$ 8.000,00
  - **São Paulo:** R$ 300,00

---

## 8. Próximas Versões

Roadmap de evolução prática na trilha pré-POO:

- [x] **Desafio 01:** Sanitizador Defensivo de Leads de Fintech (Concluído).
- [x] **Desafio 02:** Reconciliação Financeira com Deduplicação (`set`) e Detecção de Fraude Noturna (Concluído).
- [ ] **Desafio 03:** Cálculo manual de Métricas de Avaliação de Machine Learning (MAE e RMSE sem Scikit-Learn).
- [ ] **Desafio 04:** Ingestão e Auditoria de Logs de Acesso com Detecção de Ataques de Força Bruta.
- [ ] **Transição POO:** Refatoração modular orientada a objetos das soluções após o domínio da base procedimental.

---

## 👨‍💻 Autor

Desenvolvido por **[Ryan Aurélio](https://github.com/ryanaurelio2005)**.  
*Estudante de Ciência de Dados e Inteligência Artificial (PUC Goiás) | Foco em Engenharia de Machine Learning.*
