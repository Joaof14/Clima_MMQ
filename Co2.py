import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from MMQ import *

#importar dados
df = pd.read_excel('Data/final_data.xlsx')

# fazer pra CO2
y = np.array(df['Co2 ppm'])
x = np.array(df['decimal date'])

#x = np.array([1,2,3,4,5, 9])

#y = np.array([2,4,6,8,11,26])

#gerar resultados
resultado = lin(x, y)
resultados = []
resultados.append(resultado)

resultado = logaritmo(x, y)
resultados.append(resultado)

resultado = exponencial(x, y)
resultados.append(resultado)

resultado = potencial(x, y)
resultados.append(resultado)

#resultado = geometrico(x, y)
#resultados.append(resultado)

resultado = polinomial(x, y)
resultados.append(resultado)

dfresultados = pd.DataFrame(resultados, columns=['equação', 'r²'])
dfresultados.to_excel('resultadoCo2.xlsx')

