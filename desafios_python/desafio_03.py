precos_reais = [45000.0, 72000.0, "corrompido", 110000.0, 28000.0, 65000.0, ""]
precos_previstos = [43500.0, 75000.0, 80000.0, 102000.0, "erro", 64500.0, 30000.0]

def alinhar_e_limpar_predicoes(reais, previstos):

    lista_limpa1 = []
    lista_limpa2 = []

    for item1, item2 in zip(reais, previstos):

        try:
            conver1 = float(item1)
            conver2 = float(item2)

            lista_limpa1.append(conver1)
            lista_limpa2.append(conver2)

        except (ValueError, TypeError):

            continue

    return lista_limpa1, lista_limpa2

def calcular_mae(y_real, y_pred):


    previsto = 0
    diferenca = 0
    real = 0
    erro_absoluto = []
    soma = 0

    for l1, l2 in zip(y_real, y_pred):

        erro = abs(l1 -l2)

        if erro >= diferenca:

            real = l1
            previsto = l2
            diferenca = erro

        erro_absoluto.append(erro)
        soma += abs(erro)

    erro_medio = soma/len(erro_absoluto) 

    texto = f"R$ {erro_medio:.2f}"       

    return texto, real, previsto, abs(diferenca)


def calcular_rmse(y_real, y_pred):

    soma = 0
    for l1, l2 in zip(y_real, y_pred):
    
        res = (l1 - l2)**2
        soma += (res)
    
    erro_medio = soma/len(y_real)

    rmse = erro_medio**0.5 
    
    texto = f"R$ {rmse:.2f}"       
    
    return texto


if __name__ == "__main__":

    l1, l2 = alinhar_e_limpar_predicoes(precos_reais, precos_previstos)
    erro_medio, real, previsto, diferenca = calcular_mae(l1, l2)
    rmse = calcular_rmse(l1, l2)


    print("LISTAS LIMPAS:")
    print(l1)
    print(l2)
    print(f"Erro médio absoluto: {erro_medio}")
    print(f"RMSE {rmse}")
    print("Caso com maior erro individual: ")
    print(f"Valor Real: {real}")
    print(f"Vaslor Previsto: {previsto}")
    print(f"Diferença: {diferenca}")

        





