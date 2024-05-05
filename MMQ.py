# Método dos Mínimos Quadrados Linear e Ajustes não Linares

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# funções para calcular


# criar função tabela


# funções para calcular
def calcula_reg(coluna_x, coluna_y):

   # tabelamento
    n = len(coluna_x)
    soma_x = np.sum(coluna_x)
    soma_y = np.sum(coluna_y)
    soma_x2 = np.sum(coluna_x * coluna_x)
    soma_xy = np.sum(coluna_x * coluna_y)

   # calculo dos coeficientes a e b
    a = ((n * soma_xy) - (soma_x * soma_y)) / \
        ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / \
        ((soma_x * soma_x) - (n * soma_x2))

    return a, b


def calcula_r2(coluna_x, coluna_y, a, b):

    fx = a * coluna_x + b
    ym = np.mean(coluna_y)
    r2 = np.sum((fx - ym)**2) / np.sum((coluna_y - ym)**2)

    return r2



def plotgrafico( x,  y , linha, label):
    graf, eix = plt.subplots()
    eix.scatter(x,y)
    eix.plot(linha, label = label )
    eix.set_ylabel('Co2 ppm')
    eix.set_xlabel('Data')
    eix.set_title('Grafíco')
    eix.grid()
    eix.legend()
    graf.show()
    
    



def lin(x, y):
    x_ = x
    y_ = y

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    # Gráficos
    linha = a*x + b
    label = 'y = {:.4f}*x + {:.4f}\nR² = {:.4f}'.format(a, b, r2)

    plotgrafico(x, y, linha, label=label)

    
    return label

    


def logaritmo(x, y):

    x_ = np.log(x)
    y_ = y

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    # Gráficos
    linha = a*np.log(x) + b
    label = 'y = {:.4f}*log(x) + {:.4f}\nR² = {:.4f}'.format(a, b, r2)
    plotgrafico(x, y, linha, label=label)

    return label


def potencial(x, y):

    x_ = np.log(x)
    y_ = np.log(y)

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    # Conversão dos coeficientes
    b = np.exp(b)
    # Gráficos
    linha = b*x**a
    label = 'y = {:.4f}*x + {:.4f}\nR2 = {:.4f}'.format(a, b, r2)

    plotgrafico(x, y, linha, label=label)

    
    return label


def exponencial(x, y):

    y_ = np.log(y)
    x_ = x

    # Transformações (g2 e gj)

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    # Conversão dos coeficientes (se necessário)
    b = np.exp(b)
    # Gráficos
    linha = b*np.exp(a*x)

    label = 'y = {:.4f}*e**({:.4f}*x)\nR² = {:.4f}'.format(b,a, r2)

    plotgrafico(x, y, linha, label=label)

    # criar return label
    
    return label


def geometrico(x, y):

    y_ = np.log(y)
    x_ = x

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    # Conversão dos coeficientes (se necessário)
    a = np.exp(a)
    b = np.exp(b)
    # Gráficos
    linha = b*x**a

    label = 'y = {:.4f}*x**({:.4f})\nR² = {:.4f}'.format(b,a, r2)
    plotgrafico(x, y, linha, label=label)

    # criar return label
    
    return label


def polinomial(x, y, grau=2):

    n = grau + 1
    mA = np.zeros((n, n))
    mB = np.zeros(n)

    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (x**(i + j)).sum()
        mB[i] = (y * (x**(i))).sum()

    resul = np.linalg.solve(mA, mB)
    a,b,c = resul
   
    fx = np.sum(c*(x**i)for i, c in enumerate(resul))
    ym = np.mean(y)
    r2 = np.sum((fx - ym)**2) / np.sum((y - ym)**2)
    linha = fx

    label = 'y = ({:.4f}*x**2) + {:.4f}*x + {:.4f} \nR² = {:.4f}'.format(a,b,c, r2)
    plotgrafico(x, y, linha, label=label)


    return label






x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 8, 10])
pont = 5

resultado = lin(x,y)
print('Linear: ', resultado)

resultado = logaritmo(x,y)
print('Logaritmo: ', resultado)

resultado = exponencial(x,y)
print('exponencial: ', resultado)

resultado = potencial(x,y)
print('potencial: ', resultado)

resultado = geometrico(x,y)
print('geometrico: ', resultado)




#importar dados
df = pd.read_csv('Data/final_data.csv')
y = df['Co2 ppm']
x = df['decimal date']

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

resultado = geometrico(x, y)
resultados.append(resultado)

resultado = polinomial(x, y)
resultados.append(resultado)




""" 











import matplotlib.pyplot as plt
data1 = [5103020100, 5373080100, 5403020100, 5653340120, 5704020150]
data2 = [10300100, 17300100, 20300100, 26534020, 30040010]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylim(5102020100, 5704020155)
ax1.set_ylabel('GDP Country W (trillion)', color=color)
ax1.plot(data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 

color = 'tab:green'
ax2.set_ylabel('GDP City Z (million)', color=color) 
ax2.set_ylim(1300100, 100040010)
ax2.plot(data2,color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 
plt.legend()
plt.show()"""