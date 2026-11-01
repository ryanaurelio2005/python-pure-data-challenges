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

lista_limpa = []
lista_clientes = []
leads_descartados = 0 

for item_texto in leads_brutos:

    item_limpo = [item.strip() for item in item_texto.split(";")]
    lista_limpa.append(item_limpo)


for cliente in lista_limpa:

    id_txt, nome_txt, idade_txt, valor_txt, estado_txt, validacao_txt = cliente


    valor_limpo = valor_txt.replace(".", "").replace(",", ".").replace("R$", "").strip()

    

    try:


        id_cl = int(id_txt)
        idade_cl = int(idade_txt)
        valor_cl = float(valor_limpo)

        if idade_cl < 18 or valor_cl <= 0:
            leads_descartados +=1
            continue



   


        dicionario_temporario = {

        "id": id_cl,
        "nome": nome_txt.title(),
        "idade": idade_cl,
        "valor": valor_cl,
        "estado": estado_txt.upper(),
        "situacao": validacao_txt.lower()

    }

        lista_clientes.append(dicionario_temporario)

    except ValueError:
        leads_descartados += 1   
        continue

print(lista_clientes)
print(f"Quantidades de leads recebidos: {len(leads_brutos)}")
print(f"Quantidade de leads aprovados: {len(lista_clientes)}")
print(f"Quantidade de leads descartados {leads_descartados}")




