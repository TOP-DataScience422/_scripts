from matplotlib import pyplot as plt
from pandas import (
    concat,
    DataFrame,
    read_csv,
)
from statsmodels.tsa.stattools import adfuller, kpss

from datetime import timedelta as td
from pathlib import Path
from sys import path


births = read_csv(
    Path(path[0]) / 'births.csv', 
    parse_dates=True, 
    index_col='date',
)

# predicted_i = alpha * actual + (1 - alpha) * predicted_i-1

alpha = 0.2

births = concat([births, DataFrame(index=births.iloc[-1:].index + td(days=1))])
births['births_exp'] = [None] * len(births)

births.iloc[1, 1] = births.iloc[0, 0]
for i in range(2, len(births)):
    predicted = alpha * births.iloc[i-1, 0] + (1 - alpha) * births.iloc[i-1, 1]
    births.iloc[i, 1] = predicted


fig = plt.figure(layout='constrained')
axs = fig.subplots()

axs.plot(births['births'])
axs.plot(births['births_exp'], c='orange')

plt.show()

