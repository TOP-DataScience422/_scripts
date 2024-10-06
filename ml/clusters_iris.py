from matplotlib import pyplot as plt
from numpy import array
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


raw = load_iris()
data = DataFrame(raw['data'], columns=raw['feature_names'])

data_norm = (data - data.mean()) / data.std()

x = data_norm
y_test = raw['target']

model = KMeans(n_clusters=3, random_state=1)
y_pred = model.fit_predict(x)

y_pred = array([
    1 if v == 0 else (0 if v == 1 else v)
    for v in y_pred
])


fig = plt.figure(layout='constrained')
axs = fig.subplots(2, 6)

axs[0][0].scatter(data.iloc[:, 0], data.iloc[:, 1], c=y_test, cmap='Set1')
axs[1][0].scatter(data.iloc[:, 0], data.iloc[:, 1], c=y_pred, cmap='Set1')
axs[0][0].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 1].name)
axs[1][0].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 1].name)

axs[0][1].scatter(data.iloc[:, 0], data.iloc[:, 2], c=y_test, cmap='Set1')
axs[1][1].scatter(data.iloc[:, 0], data.iloc[:, 2], c=y_pred, cmap='Set1')
axs[0][1].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 2].name)
axs[1][1].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 2].name)

axs[0][2].scatter(data.iloc[:, 0], data.iloc[:, 3], c=y_test, cmap='Set1')
axs[1][2].scatter(data.iloc[:, 0], data.iloc[:, 3], c=y_pred, cmap='Set1')
axs[0][2].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 3].name)
axs[1][2].set(xlabel=data.iloc[:, 0].name, ylabel=data.iloc[:, 3].name)

axs[0][3].scatter(data.iloc[:, 1], data.iloc[:, 2], c=y_test, cmap='Set1')
axs[1][3].scatter(data.iloc[:, 1], data.iloc[:, 2], c=y_pred, cmap='Set1')
axs[0][3].set(xlabel=data.iloc[:, 1].name, ylabel=data.iloc[:, 2].name)
axs[1][3].set(xlabel=data.iloc[:, 1].name, ylabel=data.iloc[:, 2].name)

axs[0][4].scatter(data.iloc[:, 1], data.iloc[:, 3], c=y_test, cmap='Set1')
axs[1][4].scatter(data.iloc[:, 1], data.iloc[:, 3], c=y_pred, cmap='Set1')
axs[0][4].set(xlabel=data.iloc[:, 1].name, ylabel=data.iloc[:, 3].name)
axs[1][4].set(xlabel=data.iloc[:, 1].name, ylabel=data.iloc[:, 3].name)

axs[0][5].scatter(data.iloc[:, 2], data.iloc[:, 3], c=y_test, cmap='Set1')
axs[1][5].scatter(data.iloc[:, 2], data.iloc[:, 3], c=y_pred, cmap='Set1')
axs[0][5].set(xlabel=data.iloc[:, 2].name, ylabel=data.iloc[:, 3].name)
axs[1][5].set(xlabel=data.iloc[:, 2].name, ylabel=data.iloc[:, 3].name)

plt.show()

