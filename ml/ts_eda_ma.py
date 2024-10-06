from matplotlib import pyplot as plt
from pandas import read_csv

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

passengers_ma1 = passengers.rolling(4).mean()
passengers_ma2 = passengers.rolling(6).mean()
passengers_ma3 = passengers.rolling(12).mean()
passengers_ma4 = passengers.rolling(48).mean()

births_ma1 = births.rolling(7).mean()
births_ma2 = births.rolling(21).mean()
births_ma3 = births.rolling(64).mean()
births_ma4 = births.rolling(180).mean()


fig = plt.figure(figsize=(16,10), layout='constrained')
axs = fig.subplots(4, 2)

axs[0][0].plot(passengers)
axs[0][0].plot(passengers_ma1, c='r')
axs[0][0].set(title='ширина окна = 4')

axs[1][0].plot(passengers)
axs[1][0].plot(passengers_ma2, c='r')
axs[1][0].set(title='ширина окна = 6')

axs[2][0].plot(passengers)
axs[2][0].plot(passengers_ma3, c='r')
axs[2][0].set(title='ширина окна = 12')

axs[3][0].plot(passengers)
axs[3][0].plot(passengers_ma4, c='r')
axs[3][0].set(title='ширина окна = 48')

axs[0][1].plot(births)
axs[0][1].plot(births_ma1, c='r')
axs[0][1].set(title='ширина окна = 7')

axs[1][1].plot(births)
axs[1][1].plot(births_ma2, c='r')
axs[1][1].set(title='ширина окна = 21')

axs[2][1].plot(births)
axs[2][1].plot(births_ma3, c='r')
axs[2][1].set(title='ширина окна = 64')

axs[3][1].plot(births)
axs[3][1].plot(births_ma4, c='r')
axs[3][1].set(title='ширина окна = 180')

plt.show()
