"""==============================================================================
NÍVEL 2: Reconciliação Financeira e Anti-Fraude (Deduplicação & Agrupamento)
Autor: Ryan Aurélio
Objetivo: Tratar instabilidade de gateway de pagamentos com deduplicação em set,
          identificar fraudes noturnas e consolidar faturamento regional.
=============================================================================="""

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

# TODO: Desenvolver a lógica do Desafio 02:
# 1. Deduplicar usando set com tupla de unicidade (cliente, valor, hora)
# 2. Identificar transações noturnas de alto risco (> R$ 10.000 e hora >= 22 ou < 6)
# 3. Agrupar volume financeiro por cidade
