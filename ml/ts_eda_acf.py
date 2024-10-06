from matplotlib import pyplot as plt
from numpy import array
from pandas import read_csv
from statsmodels.graphics.tsaplots import plot_acf

from pathlib import Path
from sys import path


passengers = read_csv(
    Path(path[0]) / 'passengers.csv', 
    parse_dates=True, 
    index_col='month',
)
births = read_csv(
    Path(path[0]) / 'births.csv', 
    parse_dates=True, 
    index_col='date',
)

passengers_acf = []
for i in range(25):
    point = [i]
    shifted = passengers.shift(i)
    corr_coef = passengers.corrwith(shifted)
    point.extend(corr_coef)
    passengers_acf.append(point)

passengers_acf = array(passengers_acf)

births_acf = []
for i in range(90):
    point = [i]
    shifted = births.shift(i)
    corr_coef = births.corrwith(shifted)
    point.extend(corr_coef)
    births_acf.append(point)

births_acf = array(births_acf)


fig = plt.figure(layout='constrained')
axs = fig.subplots(2,2)

axs[0][0].scatter(*passengers_acf.T, c='r')
axs[0][0].set_ylim(-1.15, 1.15)

plot_acf(passengers, axs[1][0], lags=24, auto_ylims=True)

axs[0][1].scatter(*births_acf.T)
axs[0][1].set_ylim(-1.15, 1.15)

plot_acf(births, axs[1][1], lags=90, auto_ylims=True)

plt.show()
