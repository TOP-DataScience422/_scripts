from matplotlib import pyplot as plt
from numpy import linspace
from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    root_mean_squared_error as skl_rmse,
    r2_score as skl_r2,
)

from itertools import chain
from math import floor, ceil
from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'boston.csv'


boston = read_csv(data_path, comment='#')

# отбор зависимых переменных
x = boston.loc[:, ('LSTAT', 'RM')]
y = boston['MEDV']

# разделение набора данных на обучающую и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=1/3,
    random_state=2
)
assert x_test.shape[0] + x_train.shape[0] == x.shape[0]

# обучение модели
model = LinearRegression()
model.fit(x_train, y_train)

# тестирование модели
y_predict = model.predict(x_test)
assert y_predict.shape == y_test.shape


# метрики:

# среднеквадратичная ошибка
rmse = (sum((y_predict - y_test)**2) / len(y_test))**0.5
rmse_ = skl_rmse(y_test, y_predict)
assert round(rmse, 1) == round(rmse_, 1)

# коэффициент детерминации
r2 = 1 - rmse**2 * len(y_test) / sum((y_test - y_test.mean())**2)
r2_ = skl_r2(y_test, y_predict)
assert round(r2, 3) == round(r2_, 3)



# трёхмерное графическое представление функции двух переменных

# lstat_norm = (boston['LSTAT'] - boston['LSTAT'].mean()) / boston['LSTAT'].std()
# rm_norm = (boston['RM'] - boston['RM'].mean()) / boston['RM'].std()
# medv_norm = (boston['MEDV'] - boston['MEDV'].mean()) / boston['MEDV'].std()
# 
# plt_xy_min = floor(min(chain(lstat_norm, rm_norm)))
# plt_xy_max = ceil(max(chain(lstat_norm, rm_norm)))
# 
# plt_xy = linspace(plt_xy_min, plt_xy_max, 1000)
# 
# ax = plt.figure().add_subplot(projection='3d')
# ax.scatter(lstat_norm, rm_norm, medv_norm)
# ax.plot(
#     plt_xy,
#     plt_xy,
#     plt_xy*model.coef_[0] + plt_xy*model.coef_[1] + model.intercept_,
#     c='0'
# )
# 
# ax.set_xlabel('LSTAT')
# ax.set_ylabel('RM')
# ax.set_zlabel('MEDV')
# 
# plt.show()

