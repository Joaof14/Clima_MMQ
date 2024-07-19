import pandas as pd
import numpy as np

df = pd.read_excel('Data/final_data.xlsx')

def regressao_linear_multipla(X, Y):
    # Adicionar uma coluna de uns para representar o intercepto
    X = np.column_stack((np.ones(len(X)), X))
    
    # Calcular os coeficientes de regressão
    coeficientes = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
    
    return coeficientes

# Exemplo de uso
X = np.array([[1, 2], [3, 4], [5, 6]])  # Variáveis independentes
Y = np.array([3, 5, 7])  # Variável dependente

coeficientes = regressao_linear_multipla(X, Y)
print("Coeficientes:", coeficientes)

X = df[["decimal date", "CO2 ppm"]]
Y = df["temperature anomalies"]

# Aplicação da regressão linear múltipla
coeficientes = regressao_linear_multipla(X, Y)

# Interpretando os coeficientes
beta_0 = coeficientes[0]  # Intercepto
beta_1 = coeficientes[1]  # Coeficiente para a variável "tempo"
beta_2 = coeficientes[2]  # Coeficiente para a variável "CO2_ppm"

print("Coeficiente de Intercepto (beta_0):", beta_0)
print("Coeficiente para 'tempo' (beta_1):", beta_1)
print("Coeficiente para 'CO2_ppm' (beta_2):", beta_2)