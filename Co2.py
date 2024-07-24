import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

array_prev = [2034.0410, 2034.1257, 2034.2049, 2034.2896, 2034.3716, 2034.4563, 2034.5383, 2034.6230, 2034.7077, 2034.7896, 2034.8743, 2034.9563]

# funções para calcular
def calcula_reg(coluna_x, coluna_y):
    n = len(coluna_x)
    soma_x = np.sum(coluna_x)
    soma_y = np.sum(coluna_y)
    soma_x2 = np.sum(coluna_x * coluna_x)
    soma_xy = np.sum(coluna_x * coluna_y)

    a = ((n * soma_xy) - (soma_x * soma_y)) /  ((n * soma_x2) - (soma_x * soma_x))
    b = ((soma_x * soma_xy) - (soma_y * soma_x2)) / ((soma_x * soma_x) - (n * soma_x2))

    return a, b

def calcula_r2(coluna_x, coluna_y, a, b):
    fx = a * coluna_x + b
    ym = np.mean(coluna_y)
    r2 = np.sum((fx - ym)**2) / np.sum((coluna_y - ym)**2)

    return r2

def plotgrafico(x, y, linha, label):
    label = label.replace('.', ',').replace('**','^').replace('*', '.')
    graf, eix = plt.subplots()
    eix.scatter(x, y, color='black')
    eix.plot(x, linha, label=label, color='red')
    eix.set_ylabel('Co2 ppm')
    eix.set_xlabel('Data')
    eix.set_title('Grafico')
    eix.legend()
    graf.show()

def save_summary(file_name, a, b, r2_value, F, p_value_F, t_stats, p_values_t):
    with open(file_name, 'w') as file:
        file.write(f'Coeficientes: a = {a}, b = {b}\n')
        file.write(f'R²: {r2_value}\n')
        file.write(f'Estatística F: {F}\n')
        file.write(f'p-valor (F): {p_value_F}\n')
        file.write(f'Estatísticas t: {t_stats}\n')
        file.write(f'p-valores (t): {p_values_t}\n')

def lin(x, y):
    x_ = x
    y_ = y

    a, b = calcula_reg(x_, y_)
    r2_value = calcula_r2(x_, y_, a, b)
    
    linha = a * x + b
    eq = 'y = {:.6g}*x + ({:.6g})\n'.format(a, b)
    r2 = 'R² = {:.6g}'.format(r2_value)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = [a * dataFut + b for dataFut in array_prev]
    
    residuals = y - linha
    n = len(y)
    p = 2
    
    SSR = np.sum(residuals**2)
    SST = np.sum((y - np.mean(y))**2)
    
    MSR = (SST - SSR) / (p - 1)
    MSE = SSR / (n - p)
    F = MSR / MSE
    p_value_F = 1 - stats.f.cdf(F, p - 1, n - p)
    
    X = np.column_stack((np.ones(n), x))
    se = np.sqrt(MSE * np.linalg.inv(X.T @ X).diagonal())
    t_stats = np.array([a, b]) / se
    p_values_t = [2 * (1 - stats.t.cdf(np.abs(t), n - p)) for t in t_stats]
    
    save_summary('CO2_summary_lin.txt', a, b, r2_value, F, p_value_F, t_stats, p_values_t)
    
    return eq, r2, prev, a, b

def logaritmo(x, y):
    x_ = np.log(x)
    y_ = y

    a, b = calcula_reg(x_, y_)
    r2_value = calcula_r2(x_, y_, a, b)
    
    linha = a * np.log(x) + b
    eq = 'y = {:.6g}*ln(x) + ({:.6g})\n'.format(a, b)
    r2 = 'R² = {:.6g}'.format(r2_value)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = [a * np.log(dataFut) + b for dataFut in array_prev]
    
    residuals = y - linha
    n = len(y)
    p = 2
    
    SSR = np.sum(residuals**2)
    SST = np.sum((y - np.mean(y))**2)
    
    MSR = (SST - SSR) / (p - 1)
    MSE = SSR / (n - p)
    F = MSR / MSE
    p_value_F = 1 - stats.f.cdf(F, p - 1, n - p)
    
    X = np.column_stack((np.ones(n), np.log(x)))
    se = np.sqrt(MSE * np.linalg.inv(X.T @ X).diagonal())
    t_stats = np.array([a, b]) / se
    p_values_t = [2 * (1 - stats.t.cdf(np.abs(t), n - p)) for t in t_stats]
    
    save_summary('CO2_summary_log.txt', a, b, r2_value, F, p_value_F, t_stats, p_values_t)
    
    return eq, r2, prev, a, b

def potencial(x, y):
    x_ = np.log(x)
    y_ = np.log(y)

    a, b = calcula_reg(x_, y_)
    r2_value = calcula_r2(x_, y_, a, b)
    
    b = np.exp(b)
    linha = b * x**a
    eq = 'y = {:.6g}*x**({:.6g})\n'.format(b, a)
    r2 = 'R² = {:.6g}'.format(r2_value)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = [b * dataFut**a for dataFut in array_prev]
    
    residuals = y - linha
    n = len(y)
    p = 2
    
    SSR = np.sum(residuals**2)
    SST = np.sum((y - np.mean(y))**2)
    
    MSR = (SST - SSR) / (p - 1)
    MSE = SSR / (n - p)
    F = MSR / MSE
    p_value_F = 1 - stats.f.cdf(F, p - 1, n - p)
    
    X = np.column_stack((np.ones(n), np.log(x)))
    se = np.sqrt(MSE * np.linalg.inv(X.T @ X).diagonal())
    t_stats = np.array([a, b]) / se
    p_values_t = [2 * (1 - stats.t.cdf(np.abs(t), n - p)) for t in t_stats]
    
    save_summary('CO2_summary_pot.txt', a, b, r2_value, F, p_value_F, t_stats, p_values_t)
    
    return eq, r2, prev, a, b

def exponencial(x, y):
    y_ = np.log(y)
    x_ = x

    a, b = calcula_reg(x_, y_)
    r2_value = calcula_r2(x_, y_, a, b)
    
    b = np.exp(b)
    linha = b * np.exp(a * x)
    eq = 'y = {:.6g}*e**({:.6g}*x)\n'.format(b, a)
    r2 = 'R² = {:.6g}'.format(r2_value)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = [b * np.exp(a * dataFut) for dataFut in array_prev]
    
    residuals = y - linha
    n = len(y)
    p = 2
    
    SSR = np.sum(residuals**2)
    SST = np.sum((y - np.mean(y))**2)
    
    MSR = (SST - SSR) / (p - 1)
    MSE = SSR / (n - p)
    F = MSR / MSE
    p_value_F = 1 - stats.f.cdf(F, p - 1, n - p)
    
    X = np.column_stack((np.ones(n), x))
    se = np.sqrt(MSE * np.linalg.inv(X.T @ X).diagonal())
    t_stats = np.array([a, b]) / se
    p_values_t = [2 * (1 - stats.t.cdf(np.abs(t), n - p)) for t in t_stats]
    
    save_summary('CO2_summary_exp.txt', a, b, r2_value, F, p_value_F, t_stats, p_values_t)
    
    return eq, r2, prev, a, b

def polinomial(x, y, grau=2):
    n = grau + 1
    mA = np.zeros((n, n))
    mB = np.zeros(n)

    for i in range(mB.size):
        for j in range(mB.size):
            mA[i][j] = (x**(i + j)).sum()
        mB[i] = (y * (x**(i))).sum()
    mA[0][0] = x.size
    
    resul = np.linalg.solve(mA, mB)
    c, b, a = resul
   
    fx = np.sum(c * (x**i) for i, c in enumerate(resul))
    ym = np.mean(y)
    r2_value = np.sum((fx - ym)**2) / np.sum((y - ym)**2)
    
    linha = fx
    eq = 'y = ({:.6g}*x**2) + ({:.6g})*x + ({:.6g}) \n'.format(c, b, a)
    r2 = 'R² = {:.6g}'.format(r2_value)
    label = eq + r2
    
    plotgrafico(x, y, linha, label=label)

    prev = [c * dataFut**2 + b * dataFut + a for dataFut in array_prev]
    
    residuals = y - linha
    n = len(y)
    p = 3
    
    SSR = np.sum(residuals**2)
    SST = np.sum((y - np.mean(y))**2)
    
    MSR = (SST - SSR) / (p - 1)
    MSE = SSR / (n - p)
    F = MSR / MSE
    p_value_F = 1 - stats.f.cdf(F, p - 1, n - p)
    
    X = np.column_stack((np.ones(n), x, x**2))
    se = np.sqrt(MSE * np.linalg.inv(X.T @ X).diagonal())
    t_stats = np.array([a, b, c]) / se
    p_values_t = [2 * (1 - stats.t.cdf(np.abs(t), n - p)) for t in t_stats]
    
    save_summary('CO2_summary_poly.txt', a, b, r2_value, F, p_value_F, t_stats, p_values_t)
    
    return eq, r2, prev, c, b, a

#importar dados
df = pd.read_excel('Data/final_data.xlsx')

# fazer pra CO2
y = np.array(df['Co2 ppm'])
x = np.array(df['decimal date'])

#gerar resultados
coeficientesCo2 = []
resultados = []

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
                       'Mês': np.arange(1, 13), 
                       'Decimal Date': array_prev,
                       'Linear': prevLin,
                       'Exponencial': prevExp,
                       'Potencial': prevPot,
                       'PrevPol': prevPol})

dfresultados = pd.DataFrame(resultados, columns=['equação', 'r²'])
dfresultados.to_excel('resultadoCo2.xlsx')
dfPrev.to_excel("PrevCo2_x_tempo.xlsx")
