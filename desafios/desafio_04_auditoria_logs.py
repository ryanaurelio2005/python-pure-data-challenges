"""==============================================================================
NÍVEL 4: Pipeline de Ingestão de Log de Acessos & Detecção de Força Bruta
Autor: Ryan Aurélio
Objetivo: Parser textual de stream de logs, agregação estatística de status codes
          e detecção heurística de ataques de força bruta por IP.
=============================================================================="""

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

# TODO: Desenvolver a lógica do Desafio 04:
# 1. Função fazer_parse_linha(linha) com validações defensivas
# 2. Estatísticas de tráfego por status code e tempo médio
# 3. Detector de força bruta (IPs com >= 3 falhas 401)
