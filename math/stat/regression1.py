from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, dot, corrcoef
from numpy import set_printoptions

from itertools import chain
from pprint import pprint


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 16
rcParams['axes.titlesize'] = 20

set_printoptions(suppress=True)


# объём выборки
n = 100

# закон распределения случайной величины X
x = array([60, 70, 80, 90, 100])
nx = array([8, 23, 35, 20, 14])
# численные характеристики случайной величины X
x_mean = dot(x, nx) / n
x_var = dot(x**2, nx) / n - x_mean**2
x_std = x_var**0.5

# закон распределения случайной величины Y
y = array([25, 30, 35, 40, 45, 50])
my = array([3, 20, 42, 19, 14, 2])
# численные характеристики случайной величины Y
y_mean = dot(y, my) / n
y_var = dot(y**2, my) / n - y_mean**2
y_std = y_var**0.5

# корреляционная таблица
m_xy = array([
    [3, 0, 0, 0, 0],
    [5, 12, 3, 0, 0],
    [0, 11, 28, 3, 0],
    [0, 0, 4, 13, 2],
    [0, 0, 0, 4, 10],
    [0, 0, 0, 0, 2],
])

# компоненты координат точек для пар значений случайных величин X и Y
points_x = [x[j] for i in range(len(y)) for j in range(len(x)) if m_xy[i,j]]
points_y = [y[i] for i in range(len(y)) for j in range(len(x)) if m_xy[i,j]]
# альтернативный способ получения координат точек
# points_x_ = list(chain([x[j]]*sum(array(m_xy, dtype=bool)[:,j]) for j in range(len(x))))

# точечный график пар значений случайных величин X и Y
plt.scatter(points_x, points_y, s=7**2)

# центр рассеивания
plt.scatter(x_mean, y_mean, s=6.5**2, c='0')
plt.annotate('A', (x_mean, y_mean), (x_mean-1, y_mean+0.5))

# условные законы распределения случайных величин Y для каждого значения случайной величины X
y_cond_distrs = []
for j in range(len(x)):
    yd_vals, yd_m = [], []
    y_cond_distrs.append([yd_vals, yd_m])
    for i in range(len(y)):
        if m_xy[i,j]:
            yd_vals.append(y[i])
            yd_m.append(m_xy[i,j])

# >>> for yd in y_cond_distrs:
# ...     print(array(yd), end='\n\n')
# ...
# [[25 30]
#  [ 3  5]]
# 
# [[30 35]
#  [12 11]]
# 
# [[30 35 40]
#  [ 3 28  4]]
# 
# [[35 40 45]
#  [ 3 13  4]]
# 
# [[40 45 50]
#  [ 2 10  2]]

# средние выборочные условных законов распределения случайных величин Y для каждого значения случайной величины X
y_cond_distrs_means = [
    dot(yd_vals, yd_m) / nx[j]
    for j, (yd_vals, yd_m) in enumerate(y_cond_distrs)
]

# опытная линия регрессии
plt.plot(x, y_cond_distrs_means, 'D-r')

# произведение случайных величин X и Y
xy = y.reshape(6, 1) @ x.reshape(1, 5)
# среднее выборочное произведения случайных величин X и Y
xy_mean = sum(sum(xy * m_xy)) / n
# корреляционный момент
corr_moment = xy_mean - x_mean*y_mean
# коэффициент корреляции
corr_coef = corr_moment / (x_std * y_std)

# нормирование случайных величин
x_norm = (x - x_mean) / x_std
y_norm = (y - y_mean) / y_std
# численные характеристики нормированных случайных величин
x_norm_mean = y_norm_mean = 0
x_norm_var = y_norm_var = 1
x_norm_std = y_norm_std = 1

# среднее выборочное произведения нормированных случайных величин X и Y равно корреляционному моменту и коэффициенту корреляции
xy_norm = y_norm.reshape(6, 1) @ x_norm.reshape(1, 5)
xy_norm_mean = sum(sum(xy_norm * m_xy)) / n

assert round(corr_coef, 3) == round(xy_norm_mean, 3)

# теоретическая линия регрессии
plt.axline((x_mean, y_mean), slope=corr_coef*y_std/x_std, c='0')

# коэффициенты линейной функции регрессии
slope = corr_coef * y_std/x_std
intercept = y_mean - slope*x_mean

# проверочная точка на теоретической линии регрессии
x_65 = 65
y_x_65 = slope*x_65 + intercept

plt.scatter(x_65, y_x_65, s=6.5**2, c='0')
plt.annotate('B', (x_65, y_x_65), (x_65+0.5, y_x_65-1))

# развёртывание распределения случайной величины X в выборку
x_sample = []
for value, rate in zip(x, nx):
    x_sample.extend([value]*rate)
x_sample = array(x_sample)
# развёртывание распределения случайной величины Y в выборку
y_sample = []
for value, rate in zip(y, my):
    y_sample.extend([value]*rate)
y_sample = array(y_sample)

# вычисление таблицы коэффициентов корреляции Пирсона
corr_table = corrcoef(x_sample, y_sample)

# запуск GUI для отображения графиков
plt.show()
