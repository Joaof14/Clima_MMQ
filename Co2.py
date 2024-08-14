import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

array_prev = [2034.0410, 2034.1257, 2034.2049, 2034.2896, 2034.3716, 2034.4563, 2034.5383, 2034.6230, 2034.7077, 2034.7896, 2034.8743, 2034.9563]



# funções para calcular
def calcula_reg(coluna_x, coluna_y):

   # tabelamento
    n = len(coluna_x)
    soma_x = np.sum(coluna_x)
    soma_y = np.sum(coluna_y)
    soma_x2 = np.sum(coluna_x * coluna_x)
    soma_xy = np.sum(coluna_x * coluna_y)

   # calculo dos coeficientes a e b
    a = ((n * soma_xy) - (soma_x * soma_y)) /  ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / ((soma_x * soma_x) - (n * soma_x2))

    return a, b


def calcula_r2(coluna_x, coluna_y, a, b):

    fx = a * coluna_x + b
    ym = np.mean(coluna_y)
    r2 = np.sum((fx - ym)**2) / np.sum((coluna_y - ym)**2)

    return r2

def plotgrafico( x,  y , linha, label):
    label = label.replace('.', ',').replace('**','^').replace('*', '.')
    graf, eix = plt.subplots()
    eix.scatter(x,y, color = 'black')
    eix.plot(x,linha, label = label, color = 'red')
    eix.set_ylabel('Co2 ppm')
    eix.set_xlabel('Data')
    eix.set_title('Grafico')
    eix.legend()
    graf.show()






def fileText(filename, sumario):
    file = open("resultados/CO2/" +  filename + ".txt", "w")
    file.write(sumario.as_text())
    file.close()




def lin(x, y):
    x_ = x
    y_ = y
    x_ = sm.add_constant(x_)
    model = sm.OLS(y_,x_)
    res = model.fit()
    resSum = res.summary()
    fileText("Co2_linear", resSum)

    x_ = x
    y_ = y

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    #valores do ajuste
    linha = a*x + b
    eq = 'y = {:.6g}*x + ({:.6g})\n'.format(a, b)
    r2 = 'R² = {:.6g}'.format(r2)
    label = eq + r2
    
    # Gráficos
    plotgrafico(x, y, linha, label=label)

    prev = []
    
    for dataFut in array_prev:
        prev.append(a*dataFut + b)
    
    
    
    return eq, r2, prev, a,b
    

    


    


def logaritmo(x, y):

    x_ = np.log(x)
    y_ = y

    x_ = sm.add_constant(x_)
    model = sm.OLS(y_,x_)
    res = model.fit()
    resSum = res.summary()

    fileText("Co2_log", resSum)

    x_ = np.log(x)
    y_ = y

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    #valores do ajuste
    linha = a*np.log(x) + b
    eq = 'y = {:.6g}*ln(x) + ({:.6g})\n'.format(a, b)
    r2 = 'R² = {:.6g}'.format(r2)
    label = eq + r2
    ''
    # Gráficos
    plotgrafico(x, y, linha, label=label)

    prev = []
    
    for dataFut in array_prev:
        prev.append(a*np.log(dataFut) + b)

    

    return eq, r2, prev, a,b


def potencial(x, y):

    x_ = np.log(x)
    y_ = np.log(y)

    x_ = sm.add_constant(x_)
    model = sm.OLS(y_,x_)
    res = model.fit()
    resSum = res.summary()
    fileText("Co2_pot", resSum)


    x_ = np.log(x)
    y_ = np.log(y)

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    # Conversão dos coeficientes
    b = np.exp(b)
    
    #valores do ajuste
    linha = b*x**a
    eq = 'y = {:.6g}*x**({:.6g})\n'.format(b,a)
    r2 = 'R² = {:.6g}'.format(r2)
    label = eq + r2
    # Gráficos
    plotgrafico(x, y, linha, label=label)

    prev = []
   
    for dataFut in array_prev:
       prev.append(b*dataFut**a )

  
   
   # Gráficos
    plotgrafico(x, y, linha, label=label)


    return eq, r2, prev, a,b


def exponencial(x, y):

    x_ = x
    y_ = np.log(y)

    x_ = sm.add_constant(x_)
    model = sm.OLS(y_,x_)
    res = model.fit()
    resSum = res.summary()

    fileText("Co2_exp", resSum)


    y_ = np.log(y)
    x_ = x

    # Transformações (g2 e gj)

    # Calculos de coeficientes
    a, b = calcula_reg(x_, y_)
    # Calculo r2
    r2 = calcula_r2(x_, y_, a, b)
    
    # Conversão dos coeficientes (se necessário)
    b = np.exp(b)

    #valores do ajuste
    linha = b*np.exp(a*x)
    eq = 'y = {:.6g}*e**({:.6g}*x)\n'.format(b,a)
    r2 = 'R² = {:.6g}'.format(r2)
    label = eq + r2

    prev = []
    
    for dataFut in array_prev:
        prev.append(b*np.exp(a*dataFut))
    
 
    # Gráficos
    plotgrafico(x, y, linha, label=label)
 
    # criar return eq, r2
    
    return eq, r2, prev, a,b





def polinomial(x, y, grau=2):

    x_ = x
    y_ = y

    x_p = np.column_stack((x_, x_**grau))


    x_p = sm.add_constant(x_p)
    model = sm.OLS(y_,x_p)
    res = model.fit()
    resSum = res.summary()

    fileText("Co2_Quad", resSum)



    n = grau + 1
    mA = np.zeros((n, n))
    mB = np.zeros(n)

    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (x**(i + j)).sum()
        mB[i] = (y * (x**(i))).sum()
    mA[0][0] = x.size
    
    resul = np.linalg.solve(mA, mB)
    a,b,c = resul
   
    fx = np.sum(c*(x**i)for i, c in enumerate(resul))
    ym = np.mean(y)
    r2 = np.sum((fx - ym)**2) / np.sum((y - ym)**2)
    
    #valores do ajuste
    linha = fx
    eq = 'y = ({:.6g}*x**2) + ({:.6g})*x + ({:.6g}) \n'.format(c,b,a)
    r2 = 'R² = {:.6g}'.format(r2)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = []
    for dataFut in array_prev:
         prev.append(c*dataFut**2 + b*dataFut + a)
   
    return eq, r2, prev, c, b, a











#importar dados
df = pd.read_excel('Data/final_data.xlsx')

# fazer pra CO2
y = np.array(df['Co2 ppm'])
x = np.array(df['decimal date'])

#x = np.array([1,2,3,4,5, 9])

#y = np.array([2,4,6,8,11,26])

#gerar resultados
coeficientesCo2 = []
resultados = []
#gerar resultados


resultado = lin(x, y)
resultados.append(resultado[:2])

coeficientesCo2.append(resultado[3:])
prevLin = resultado[2]



resultado = logaritmo(x, y)
resultados.append(resultado[:2])

coeficientesCo2.append(resultado[3:])
prevLog = resultado[2]



resultado = exponencial(x, y)
resultados.append(resultado[:2])

coeficientesCo2.append(resultado[3:])
prevExp = resultado[2]



resultado = potencial(x, y)
resultados.append(resultado[:2])

coeficientesCo2.append(resultado[3:])
prevPot = resultado[2]



resultado = polinomial(x, y)
resultados.append(resultado[:2])

coeficientesCo2.append(resultado[3:]) 
prevPol = resultado[2]




dfPrev = pd.DataFrame({'Ano': np.ones(12)*2034, 
                       'Mês': np.arange(1,13), 
                       'Decimal Date': array_prev,
                       'Linear': prevLin,
                       'Exponencial': prevExp,
                       'Potencial': prevPot,
                       'PrevPol': prevPol
                       
                       })

dfresultados = pd.DataFrame(resultados,columns=['equação', 'r²'])
dfresultados.to_excel('resultadoCo2.xlsx')
dfPrev.to_excel("PrevCo2_x_tempo.xlsx")
