"""==============================================================================
NÍVEL 3: O Mini-Motor de Métricas de Machine Learning (Funções & Redução)
Autor: Ryan Aurélio
Objetivo: Implementar do zero o cálculo das métricas MAE e RMSE sem Scikit-Learn,
          com alinhamento e limpeza defensiva de predições corrompidas.
=============================================================================="""

precos_reais = [45000.0, 72000.0, "corrompido", 110000.0, 28000.0, 65000.0, ""]
precos_previstos = [43500.0, 75000.0, 80000.0, 102000.0, "erro", 64500.0, 30000.0]

# TODO: Desenvolver a lógica do Desafio 03:
# 1. Função alinhar_e_limpar_predicoes(reais, previstos)
# 2. Função calcular_mae(y_real, y_pred)
# 3. Função calcular_rmse(y_real, y_pred)
# 4. Identificar o maior erro individual
