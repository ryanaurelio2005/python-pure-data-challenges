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

def fazer_parse_linha(linha):

    lista_limpa = []
    lista_valores = {}
    soma_ms = 0
    carregados = 0
    nao_carregaos = 0
    processados = 0
    qtd_200 = 0
    dic_alerta = {}
    lista_alerta = []

    for log in linha:

        item_limpo = [item.strip() for item in log.split("|")]
        processados += 1

        try:

            timestamp, ip, metodo_rota, status, tempo = item_limpo
            tempo_limpo = tempo.replace("ms", "")
            status_code = int(status)
            tempo_ms = int(tempo_limpo)

            registro = {

                "TimeStamp": timestamp,
                "ip": ip,
                "Metodo_Rota": metodo_rota,
                "Status_Code": status_code,
                "Tempo[MS]": tempo_ms
                
            }

            lista_limpa.append(registro)

            carregados += 1

        except (ValueError, TypeError):

            nao_carregaos += 1
            continue

    for item in lista_limpa:

        ip_alerta = item["ip"]

        status = item["Status_Code"] 
  
        if status not in lista_valores:
             
             lista_valores[status] = 1
             
        else:

            lista_valores[status] += 1

    for item in lista_limpa:

        if item["Status_Code"] == 200:

            soma_ms += item["Tempo[MS]"]
            qtd_200 += 1

    soma_final_ms = soma_ms / qtd_200 


    for item in lista_limpa:

        code = item["Status_Code"]

        if code == 401:
            ip_stats = item["ip"]

            if ip_stats not in dic_alerta:

                dic_alerta[ip_stats] = 1
                
            else:

                dic_alerta[ip_stats] += 1

    for ip, valor_chave in dic_alerta.items():

        if valor_chave >= 3:

            lista_alerta.append((ip, valor_chave))

    return lista_limpa, carregados, nao_carregaos, processados, lista_valores, soma_final_ms, lista_alerta


if __name__ == "__main__":

    limpa, carregados, nao_carregados, processados, lista_valores, soma_final_ms, lista_alerta = fazer_parse_linha(logs_servidor)

    print("=" * 60)
    print("         RELATÓRIO DE SEGURANÇA E PERFORMANCE")
    print("=" * 60)
    print(f"Total de logs processados   : {processados}")
    print(f"Logs válidos carregados     : {carregados}")
    print(f"Logs corrompidos ignorados  : {nao_carregados}")

    print("\n--- DISTRIBUIÇÃO DE STATUS HTTP ---")
    descricoes = {200: "Sucesso", 401: "Não Autorizado", 404: "Não Encontrado"}
    for status, qtd in lista_valores.items():
        desc = descricoes.get(status, "Outro")
        print(f"  • Código {status} ({desc}): {qtd} requisições")

    print("\n--- PERFORMANCE ---")
    print(f"  • Tempo médio de resposta (status 200): {soma_final_ms:.2f} ms")

    print("\n--- AUDITORIA DE SEGURANÇA (FORÇA BRUTA DETECTADA) ---")
    for ip, qtd in lista_alerta:
        print(f"  [ALERTA] IP {ip} bloqueado com {qtd} falhas de autenticacao!")
    print("=" * 60)
