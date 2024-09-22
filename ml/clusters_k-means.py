from matplotlib import (
    pyplot as plt, 
    rcParams,
)
from numpy import array
from pandas import read_csv

from pathlib import Path
from random import uniform
from sys import path
from time import sleep


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18

filepath = Path(path[0]) / 'test_clusters.csv'

data = read_csv(filepath)
data.columns = ['x1', 'x2']


plt.ion()

fig = plt.figure(
    num='', 
    figsize=(10, 10)
)
axs = fig.add_subplot()


# выбор равноудалёных центроид
c1 = data.min().to_list()
c2 = data.max().to_list()
c3 = [data['x1'].mean(), data['x2'].mean()]

# случайный выбор центроид
c1 = [uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())]
c2 = [uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())]
c3 = [uniform(data['x1'].min(), data['x1'].max()), uniform(data['x2'].min(), data['x2'].max())]

axs.set(title='исходные данные')
axs.scatter(data['x1'], data['x2'])
axs.scatter(c1[0], c1[1], c='r', marker='^', s=100)
axs.scatter(c2[0], c2[1], c='r', marker='^', s=100)
axs.scatter(c3[0], c3[1], c='r', marker='^', s=100)
plt.draw()
plt.gcf().canvas.flush_events()
sleep(3)

for _ in range(10):
    
    cl1, cl2, cl3 = [], [], []
    for i in range(len(data)):
        d1 = ((data.iloc[i]['x1'] - c1[0])**2 + (data.iloc[i]['x2'] - c1[1])**2)**0.5
        d2 = ((data.iloc[i]['x1'] - c2[0])**2 + (data.iloc[i]['x2'] - c2[1])**2)**0.5
        d3 = ((data.iloc[i]['x1'] - c3[0])**2 + (data.iloc[i]['x2'] - c3[1])**2)**0.5
        d = min(d1, d2, d3)
        if d == d1:
            cl1.append(data.iloc[i].to_list())
        elif d == d2:
            cl2.append(data.iloc[i].to_list())
        elif d == d3:
            cl3.append(data.iloc[i].to_list())
    
    cl1 = array(cl1)
    cl2 = array(cl2)
    cl3 = array(cl3)
    
    axs.clear()
    axs.set(title='все точки отнесены к кластерам\nна основании минимального расстояния\nдо соответствующей центроиды')
    axs.scatter(cl1.T[0], cl1.T[1], c='#ff8c00')
    axs.scatter(c1[0], c1[1], c='#ff8c00', marker='^', s=100)
    axs.scatter(cl2.T[0], cl2.T[1], c='#006400')
    axs.scatter(c2[0], c2[1], c='#006400', marker='^', s=100)
    axs.scatter(cl3.T[0], cl3.T[1], c='#1e90ff')
    axs.scatter(c3[0], c3[1], c='#1e90ff', marker='^', s=100)
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(3)
    
    c1 = [cl1.T[0].mean(), cl1.T[1].mean()]
    c2 = [cl2.T[0].mean(), cl2.T[1].mean()]
    c3 = [cl3.T[0].mean(), cl3.T[1].mean()]
    
    axs.clear()
    axs.set(title='для каждого кластера вычислена новая центроида')
    axs.scatter(cl1.T[0], cl1.T[1], c='#ff8c00')
    axs.scatter(c1[0], c1[1], c='#ff8c00', marker='^', s=100)
    axs.scatter(cl2.T[0], cl2.T[1], c='#006400')
    axs.scatter(c2[0], c2[1], c='#006400', marker='^', s=100)
    axs.scatter(cl3.T[0], cl3.T[1], c='#1e90ff')
    axs.scatter(c3[0], c3[1], c='#1e90ff', marker='^', s=100)
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(3)


plt.ioff()
plt.show()

