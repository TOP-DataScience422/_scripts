from matplotlib import pyplot as plt
from pandas import (
    DataFrame,
    read_csv,
)
from statsmodels.tsa.seasonal import seasonal_decompose

from datetime import date
from pathlib import Path
from sys import path


passengers = read_csv(
    Path(path[0]) / 'passengers.csv', 
    parse_dates=True, 
    index_col='month',
)

window_width = 12
passengers_ma = passengers.rolling(window_width).mean()

passengers_seasonal1 = passengers - passengers_ma

passengers_seasonal2 = DataFrame(index=passengers.index, columns=['passengers'])
for i in range(len(passengers) - window_width):
    seasonal_group_mean = passengers_seasonal1.iloc[i::window_width].mean()
    passengers_seasonal2.iloc[i] = seasonal_group_mean
passengers_seasonal2 = passengers_seasonal2.shift(window_width)

passengers_residuals = passengers - passengers_ma - passengers_seasonal2


fig = plt.figure(figsize=(8,10), layout='constrained')
axs = fig.subplots(4, 1)

left, right = date(1948, 6, 1), date(1961, 6, 1)

axs[0].plot(passengers)
axs[0].set(xlim=(left, right), ylabel='passengers')
axs[1].plot(passengers_ma)
axs[1].set(xlim=(left, right), ylabel='trend')
axs[2].plot(passengers_seasonal2)
axs[2].set(xlim=(left, right), ylabel='seasonal')
axs[3].scatter(passengers_residuals.index, passengers_residuals['passengers'])
axs[3].set(xlim=(left, right), ylabel='residuals')

seasonal_decompose(passengers, period=window_width).plot()

plt.show()
