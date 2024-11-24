from matplotlib import pyplot as plt
from numpy import (
    array,
    linspace, 
    sin,
)
from numpy.random import normal
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from random import sample


def f(x):
    true = x * sin(x)
    biased = true + normal(size=x.shape)
    return true, biased


def train_model(model_cls, *data, **params):
    x_train, x_test, y_train, y_test = train_test_split(*data)
    model = model_cls(**params)
    model.fit(x_train, y_train)
    return model, x_test, y_test


# размер выборки
n = 101
x = linspace(-10, 10, n)
y_true, y_biased = f(x)


# размер подвыборки
k = int(n * 0.4)
# количество подвыборок = количество итераций обучения модели
N = 80
# результаты предсказания значений функции моделями на различных подвыборках
y_predictions_1 = []
for _ in range(N):
    # формирование подвыборки
    subsample = sample(array([x, y_biased]).T.tolist(), k=k)
    x_sub, y_sub = array(subsample).T
    # обучение модели
    model, _, _ = train_model(
        DecisionTreeRegressor,
        x_sub.reshape(-1, 1), 
        y_sub, 
        max_depth=7, 
    )
    # регрессия
    y_pred = model.predict(x.reshape(-1, 1))
    y_predictions_1.append(y_pred)

y_pred_mean_1 = array(y_predictions_1).mean(axis=0)


y_predictions_2 = []
for _ in range(N):
    model, _, _ = train_model(
        BaggingRegressor,
        x.reshape(-1, 1), 
        y_biased,
        estimator=DecisionTreeRegressor(max_depth=7),
        n_estimators=k,
        n_jobs=-1,
    )
    y_pred = model.predict(x.reshape(-1, 1))
    y_predictions_2.append(y_pred)

y_pred_mean_2 = array(y_predictions_2).mean(axis=0)


# применить регресионные метрики, оценить эффективность работы моделей

# вариьровать параметры моделей: максимальная глубина дерева решений, количество подвыборок — оценивать эффективность

# сравнить полученные пошагово в предыдущих двух подходах результаты с работой специализированного класса sklearn.ensemble.RandomForestRegressor


plots = 3
fig = plt.figure(figsize=(6*plots, 5))
axs = fig.subplots(1, plots)

axs[0].plot(x, y_true, lw=3)
axs[0].scatter(x, y_biased, s=10 ,c='0.6')

for y in y_predictions_1:
    axs[1].plot(x, y, lw=0.1, c='#ee82ee')
axs[1].plot(x, y_true, lw=3)
axs[1].plot(x, y_pred_mean_1, lw=2, c='#ffa500')


for y in y_predictions_2:
    axs[2].plot(x, y, lw=0.1, c='#ee82ee')
axs[2].plot(x, y_true, lw=3)
axs[2].plot(x, y_pred_mean_1, lw=2, c='#ffa500')

plt.show()

