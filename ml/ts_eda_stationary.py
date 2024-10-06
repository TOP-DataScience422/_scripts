from pandas import read_csv
from statsmodels.tsa.stattools import adfuller, kpss

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

# тест Дики-Фуллера:
# H0 — ряд нестационарный
# H1 — ряд стационарный

passengers_is_stationary_adfuller = adfuller(passengers)
births_is_stationary_adfuller = adfuller(births)

# тест KPSS:
# H0 — ряд стационарный
# H1 — ряд нестационарный

passengers_is_stationary_kpss = kpss(passengers)
births_is_stationary_kpss = kpss(births)


# >>> passengers_is_stationary_adfuller[1]
# np.float64(0.991880243437641)
# p-value > 0.05, следовательно H0 не может быть отвергнута, ряд нестационарный

# >>> passengers_is_stationary_kpss[1]
# np.float64(0.01)
# p-value < 0.05, следовательно H0 отвергается, ряд нестационарный

# совпадение тестов, всё в порядке, ряд точно нестационарный


# >>> births_is_stationary_adfuller[1]
# np.float64(5.2434129901498554e-05)
# p-value < 0.05, следовательно H0 отвергается, ряд стационарный

# >>> births_is_stationary_kpss[1]
# np.float64(0.01)
# p-value < 0.05, следовательно H0 отвергается, ряд нестационарный

# несовпадение тестов, требуются дополнительные действия с рядом (расширение, обрезание, дифференцирование, ...)

