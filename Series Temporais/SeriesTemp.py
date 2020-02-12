import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as ts
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

data = pd.read_excel('teste.xls')

def acf_pacf(x, lag = 41):
    ACF, q, pq = ts.acf(x, qstat=True, fft = False)
    tabela = np.c_[range(1,lag), ACF[1:], q, pq]
    tabela = pd.DataFrame(tabela, columns=['lag', "AC", "Q", "Prob(>Q)"])
    return tabela
    
def grafico_auto(x, lag = 36):    
    fig, ax = plt.subplots(2,1, figsize=(15,5.5))
    
    fig = plot_acf(x, lags=lag, zero=False, ax=ax[0])
    fig = plot_pacf(x, lags=lag, zero=False, ax=ax[1])
    plt.show()
    return fig, ax
    
def Modelo(x, p, q):
    modelo = sm.tsa.ARMA(x, (p, q))
    modelo =  modelo.fit()
    dw = sm.stats.durbin_watson(modelo.resid.values)
    sumario = modelo.summary()
    return [modelo, dw, sumario]

def residuos(data):
    modelo = sm.tsa.ARMA(x, (p, q))
    modelo =  modelo.fit()
    resid = modelo.resid
    ACF, q, pq = ts.acf(resid, qstat=True, fft = False)
    tabela = np.c_[range(1,41), ACF[1:], q, pq]
    tabela = pd.DataFrame(tabela, columns=['lag', "ACF", "Q", "Prob(>Q)"])
    
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(15,5.5))

    fig = plot_acf(resid, lags=40, zero=False, ax=ax1)
    fig = plot_pacf(resid, lags=40, zero=False, ax=ax2)
    plt.show()
    
    return tabela
