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

def processar_reconciliacao(logs):

    transacao_atual = set()
    transacoes_unicas = []
    transacoes_deduplicadas = 0
    transacoes_alerta = []
    somatorio = {}



    for lead in logs:

        tupla_temp = (lead["cliente"], lead["valor"], lead["hora"])
        tupla_alerta = (lead["cliente"], lead["valor"], lead["cidade"])

        if tupla_temp not in transacao_atual:

            transacao_atual.add(tupla_temp)

            transacoes_unicas.append(lead)

            if lead["valor"] > 10000.0 and (lead["hora"] >= 22 or lead["hora"] < 6):
            
                    transacoes_alerta.append(tupla_alerta)

            cidade = lead["cidade"]
        

            if cidade not in somatorio:

                somatorio[cidade] = 0.0

            somatorio[cidade] += lead["valor"]

        else:
            transacoes_deduplicadas += 1


    return transacoes_unicas, transacoes_deduplicadas, transacoes_alerta, somatorio

if __name__ == "__main__":
     
    transacoes_unicas, transacoes_deduplicadas, transacoes_alerta, somatorio = processar_reconciliacao(logs_transacoes)

    print(f"Transaçoes processadas: {len(transacoes_unicas)} | Transaçoes deduplicadas: {transacoes_deduplicadas}")
    print(f"Lista de alertas de fraudes noturnos:\n {transacoes_alerta}")
    print(f"Faturamento total consolidado por cidade:\n{somatorio}")