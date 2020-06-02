import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as ts
import matplotlib.pyplot as plt

data = pd.read_excel('Custos real de vagao_serie 1.xls')
data['log_custo'] = data['custo'].apply(lambda x: np.log(x))

modelo = sm.tsa.ARMA(data['log_custo'], (1,0), exog = data['d_2004_01'])
modelo = modelo.fit(method = "css")
print(modelo.summary())

exog_forecast = data['d_2004_01'].iloc[-12:]
forecast = modelo.forecast(12, exog = exog_forecast)
prev_out_log = forecast[0]
se_out_log = forecast[1]
linf_log = forecast[2][:,0]
lsup_log = forecast[2][:,1]
tabela = np.c_[prev_out_log, se_out_log, linf_log, lsup_log]

forecast_log = pd.DataFrame(tabela, columns = ["Forecast", "se", "linf", "lsup"])

prev_out = np.exp(forecast_log["Forecast"] + forecast_log["se"]/2)
lsup = np.exp(forecast_log["lsup"])
linf = np.exp(forecast_log["linf"])

tabela = np.c_[prev_out, linf, lsup]
forecast_custo = pd.DataFrame(tabela, columns = ["Forecast", "linf", "lsup"])
print(forecast_custo)

x1 = range(1, len(data) + 1)
x2 = range(len(data) + 1, len(data) + 13)
fig, axes  =  plt.subplots(figsize = (15, 5))
axes.plot(x1, data['custo'], 'r', label = 'Valor Observado') 
axes.plot(x2, prev_out, 'g' , label = 'Previsão')
axes.plot(x2, lsup, 'b--' , label = 'IC')
axes.plot(x2, linf, 'b--' , label = 'IC')
axes.legend()
plt.show()