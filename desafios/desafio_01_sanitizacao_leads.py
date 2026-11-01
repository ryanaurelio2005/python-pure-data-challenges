"""==============================================================================
NÍVEL 1: O Sanitizador Defensivo de Leads (Fintech)
Autor: Ryan Aurélio
Objetivo: Limpar, validar e padronizar leads brutos de formulários web usando
          Python Puro (sem Pandas/Numpy) para alimentar modelos de crédito.
=============================================================================="""

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


def processar_leads(lista_bruta):
    """Processa uma lista de leads textuais, aplicando validações defensivas de crédito.

    Regras de Negócio:
    1. ID deve ser numérico inteiro válido e não vazio.
    2. Idade deve ser numérica e maior ou igual a 18 anos.
    3. Renda deve ser convertida com sucesso para float e maior que zero.
    4. Nome padronizado em Title Case.
    5. Estado em maiúsculas (UF).
    6. Situação em minúsculas.
    """
    lista_limpa = []
    lista_clientes = []
    leads_descartados = 0

    # Etapa 1: Quebra de delimitadores ';' e remoção de espaços nas bordas
    for item_texto in lista_bruta:
        item_limpo = [item.strip() for item in item_texto.split(";")]
        lista_limpa.append(item_limpo)

    # Etapa 2: Validação de tipos e aplicação das regras de negócio
    for cliente in lista_limpa:
        id_txt, nome_txt, idade_txt, valor_txt, estado_txt, validacao_txt = cliente

        # Limpeza do formato monetário brasileiro (R$ 4.500,00 -> 4500.00)
        valor_limpo = valor_txt.replace(".", "").replace(",", ".").replace("R$", "").strip()

        try:
            id_cl = int(id_txt)
            idade_cl = int(idade_txt)
            valor_cl = float(valor_limpo)

            # Filtro de elegibilidade: maioridade e renda estritamente positiva
            if idade_cl < 18 or valor_cl <= 0:
                leads_descartados += 1
                continue

            dicionario_temporario = {
                "id": id_cl,
                "nome": nome_txt.title(),
                "idade": idade_cl,
                "valor": valor_cl,
                "estado": estado_txt.upper(),
                "situacao": validacao_txt.lower(),
            }

            lista_clientes.append(dicionario_temporario)

        except ValueError:
            # Captura falhas de coerção: texto em campos numéricos ou valores vazios
            leads_descartados += 1
            continue

    return lista_clientes, leads_descartados


if __name__ == "__main__":
    leads_aprovados, descartados = processar_leads(leads_brutos)

    print("=" * 60)
    print("      RELATÓRIO DE SANITIZAÇÃO DE LEADS (FINTECH)")
    print("=" * 60)
    print("\n[LEADS VÁLIDOS HOMOLOGADOS]:")
    for lead in leads_aprovados:
        print(f"  • ID {lead['id']:03d} | {lead['nome']:<16} | Idade: {lead['idade']} | Renda: R$ {lead['valor']:>9.2f} | UF: {lead['estado']} | Status: {lead['situacao']}")

    print("\n" + "-" * 60)
    print(f"Total de leads brutos recebidos : {len(leads_brutos)}")
    print(f"Total de leads aprovados        : {len(leads_aprovados)} ({len(leads_aprovados)/len(leads_brutos)*100:.1f}%)")
    print(f"Total de leads descartados      : {descartados} ({descartados/len(leads_brutos)*100:.1f}%)")
    print("=" * 60)
