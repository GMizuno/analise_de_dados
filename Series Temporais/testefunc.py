import SeriesTemp as st
import matplotlib.pyplot as plt
import pandas as pd
import os

print(os.getcwd())

data = pd.read_excel('teste.xls')
data['Var1'] = data['Var1'].apply(lambda x: round(x, 4))

# Testando funcao acf_pacf
print(st.acf_pacf(data['Var1']))

# Testando funcao grafico_auto
st.grafico_auto(data['Var1'])

# Testando funcao modelo
print(st.Modelo(data, 0, 1)[1])







