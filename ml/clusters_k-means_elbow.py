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


colors = [
    '#FF4500',
    '#006400',
    '#483D8B',
    '#800570',
    '#FFA500',
    '#7CFC00',
    '#87CEEB',
    '#DDA0DD',
]


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18

filepath = Path(path[0]) / 'test_clusters.csv'

data = read_csv(filepath)
data.columns = ['x1', 'x2']


plt.ion()

fig = plt.figure(
    num='', 
    figsize=(18, 9)
)
axs = fig.subplots(1, 2)


centroids: list[tuple[float, float]] = []
clusters: list[list[tuple[float, float]]] = []

wcsd = []

for c in range(1, 9):
    # c — количество кластеров и центроид

    centroids = [
        [
            uniform(data['x1'].min(), data['x1'].max()), 
            uniform(data['x2'].min(), data['x2'].max())
        ]
        for _ in range(c)
    ]

    axs[0].clear()
    axs[0].set(title='исходные данные')
    axs[0].scatter(data['x1'], data['x2'])
    for k in range(c):
        axs[0].scatter(centroids[k][0], centroids[k][1], c='r', marker='^', s=100)
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(1.5)

    for _ in range(10):
        
        clusters = [[] for _ in range(c)]
        
        for i in range(len(data)):
        
            distances = []
            for k in range(c):
                dx = data.iloc[i]['x1'] - centroids[k][0]
                dy = data.iloc[i]['x2'] - centroids[k][1]
                distances.append((dx**2 + dy**2)**0.5)
                k_min = distances.index(min(distances))
            clusters[k_min].append(data.iloc[i].to_list())
        
        for k in range(c):
            clusters[k] = array(clusters[k])
        
        axs[0].clear()
        axs[0].set(title='все точки отнесены к кластерам\nна основании минимального расстояния\nдо соответствующей центроиды')
        for k in range(c):
            if len(clusters[k]) > 0:
                axs[0].scatter(clusters[k].T[0], clusters[k].T[1], c=colors[k])
            axs[0].scatter(centroids[k][0], centroids[k][1], c=colors[k], marker='^', s=100)
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(1)
        
        for k in range(c):
            if len(clusters[k]) > 0:
                centroids[k] = [clusters[k].T[0].mean(), clusters[k].T[1].mean()]
        
        axs[0].clear()
        axs[0].set(title='для каждого кластера вычислена новая центроида')
        for k in range(c):
            if len(clusters[k]) > 0:
                axs[0].scatter(clusters[k].T[0], clusters[k].T[1], c=colors[k])
            axs[0].scatter(centroids[k][0], centroids[k][1], c=colors[k], marker='^', s=100)
        plt.draw()
        plt.gcf().canvas.flush_events()
        sleep(1)
    
    total = 0
    for k in range(c):
        for point in clusters[k]:
            dx = point[0] - centroids[k][0]
            dy = point[1] - centroids[k][1]
            total += (dx**2 + dy**2)**0.5
    wcsd.append(total)
    
    axs[1].clear()
    axs[1].plot(range(1, c+1), wcsd, '.-r', ms=10)
    plt.draw()
    plt.gcf().canvas.flush_events()
    sleep(2)


plt.ioff()
plt.show()

