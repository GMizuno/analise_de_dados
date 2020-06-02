import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as ts
import matplotlib.pyplot as plt

data = pd.read_excel('Custos real de vagao_serie 1.xls')
data['log_custo'] = data['custo'].apply(lambda x: np.log(x))

ar = 1
ma = (0, 0, 0, 1)

modelo = sm.tsa.statespace.SARIMAX(data['log_custo'], order = (ar, 0, ma), trend = 'c', exog = data['d_2004_01']).fit()
print(modelo.summary())

exog_forecast = data['d_2004_01'].iloc[-12:].to_frame()
forecast_log = modelo.get_forecast(steps = 12, exog = exog_forecast)
print(forecast_log.summary_frame())

print(dir(forecast_log.conf_int()))

prev_out_log = forecast_log.predicted_mean 
se_out_log = forecast_log.se_mean
linf_log = forecast_log.conf_int()['lower log_custo']
lsup_log = forecast_log.conf_int()['upper log_custo']
tabela = np.c_[prev_out_log, se_out_log, linf_log, lsup_log]

forecast_log = pd.DataFrame(tabela, columns = ["Forecast", "se", "linf", "lsup"])

prev_out = np.exp(forecast_log["Forecast"] + forecast_log["se"]/2)
lsup = np.exp(forecast_log["lsup"])
linf = np.exp(forecast_log["linf"])

x1 = range(1, len(data) + 1)
x2 = range(len(data) + 1, len(data) + 13)
fig, axes  =  plt.subplots(figsize = (15, 5))
axes.plot(x1, data['custo'], 'r', label = 'Valor Observado') 
axes.plot(x2, prev_out, 'g' , label = 'Previsão')
axes.plot(x2, lsup, 'b--' , label = 'IC')
axes.plot(x2, linf, 'b--' , label = 'IC')
axes.legend()
plt.show()