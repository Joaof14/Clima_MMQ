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



def plotgrafico( x,  y , linha, label, filename):
    graf, eix = plt.subplots()
    eix.scatter(x,y)
    eix.plot(x, linha, label = label )
    eix.ylabel('autovalores')
    eix.xlabel('iterações')
    eix.set_title('Grafíco')
    eix.grid()
    eix.legend()
    
    
    



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

    plotgrafico(x_, y_, linha, label=label)

    
    return a,b, linha, r2

    


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
    plotgrafico(x_, y_, linha, label=label)

    return a,b, linha, r2


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

    plotgrafico(x_, y_, linha, label=label)

    
    return a,b, linha, r2


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

    plotgrafico(x_, y_, linha, label=label)

    # criar return a,b, linha, r2
    
    return a,b, linha, r2


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
    plotgrafico(x_, y_, linha, label=label)

    # criar return a,b, linha, r2
    
    return a,b, linha, r2


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


    return a,b, linha, r2


