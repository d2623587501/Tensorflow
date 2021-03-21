import tushare as ts
import matplotlib.pyplot as plt

df1 = ts.get_k_data('600519', ktype='D', start='2010-11-12', end='2020-11-12')
print(df1.shape)
print(df1)
datapath1 = "./SH600519.csv"
df1.to_csv(datapath1)
