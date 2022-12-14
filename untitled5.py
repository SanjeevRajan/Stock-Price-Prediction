# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kqj3VsvoYiALlK88YUjAphnfFgZNRsiK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dats
from datetime import datetime
import plotly.graph_objects as go
import math


df=pd.read_csv("/content/portfolio_data.csv")
df=df.to_dict('list')
Date=df['Date']
x1=df['AMZN']
x2=df['DPZ']
x3=df['BTC']
x4=df['NFLX']
Date_time=[]
for i in Date:
    Date_time.append(i.split('/'))
time=[datetime(int(Date_time[i][2]),int(Date_time[i][0]),int(Date_time[i][1])) for i in range(len(x1))]
print(time)
    

dates=dats.date2num(time)
print(dates)
plt.plot(dates,x1)
plt.show()
plt.plot(dates,x2)
plt.show()
plt.plot(dates,x3)

plt.plot(dates,x4)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dats
from datetime import datetime
import plotly.graph_objects as go
import math


df=pd.read_csv("/content/TSLA.csv")
df=df.to_dict('list')
Date=df['Date']
High=df['High']
Low=df['Low']
Open=df['Open']
Close=df['Close']
Volume=df['Volume']
Adj_Close=df['Adj Close']
Date_time=[]
for i in Date:
    Date_time.append(i.split('-'))
time=[datetime(int(Date_time[i][0]),int(Date_time[i][1]),int(Date_time[i][2])) for i in range(len(High))]
dates=dats.date2num(time)
plt.plot(dates,High)
plt.show()

# Commented out IPython magic to ensure Python compatibility.
from statsmodels.tsa.stattools import adfuller
# %matplotlib inline
series=[[Low[i]] for i in range(len(Low))]
result = adfuller(series, autolag='AIC')
print(f'ADF Statistic: {result[0]}')
print(f'n_lags: {result[1]}')
print(f'p-value: {result[1]}')
for key, value in result[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')

print(result)

from statsmodels.tsa.stattools import kpss
def kpss_test(series, **kw):    
    statistic, p_value, n_lags, critical_values = kpss(series, **kw)
    # Format Output
    print(f'KPSS Statistic: {statistic}')
    print(f'p-value: {p_value}')
    print(f'num lags: {n_lags}')
    print('Critial Values:')
    for key, value in critical_values.items():
        print(f'   {key} : {value}')
    print(f'Result: The series is {"not " if p_value < 0.05 else ""}stationary')

kpss_test(series)
print(kpss(series))

import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

df=pd.read_csv("/content/TSLA.csv")
dic=df.to_dict('list')
d={}
d['High']=dic['High']
d['Low']=dic['Low']
d['Open']=dic['Open']
d['Close']=dic['Close']
ndf=pd.DataFrame.from_dict(d)

Series=np.array(Low)
# Import data
#df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/wwwusage.csv', names=['value'], header=0)

# Original Series
fig, axes = plt.subplots(3, 2, sharex=True)
axes[0, 0].plot(Low); axes[0, 0].set_title('Original Series')
plot_acf(ndf['High'], ax=axes[0, 1])

# 1st Differencing
axes[1, 0].plot(ndf['High'].diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(ndf['High'].diff().dropna(), ax=axes[1, 1])
print(kpss_test(ndf['High'].diff()))
# 2nd Differencing
axes[2, 0].plot(ndf['High'].diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
plot_acf(ndf['High'].diff().diff().dropna(), ax=axes[2, 1])
print(kpss_test(ndf['High'].diff().diff()))
plt.show()

ndf['High'][0:100]