from matplotlib import pyplot as plt
from numpy import array
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import homogeneity_completeness_v_measure


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

result = DataFrame(array([y_test, y_pred]).T, columns=['test', 'predicted'])
result['match'] = result['test'] == result['predicted']

print(result['match'].value_counts(normalize=True).round(2))

h, c, v = homogeneity_completeness_v_measure(y_test, y_pred)
print(
    '',
    f'гомогенность = {h:.2f}',
    f'полнота = {c:.2f}',
    f'V-мера = {v:.2f}',
    sep='\n'
)


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

