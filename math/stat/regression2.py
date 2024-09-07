from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array
from numpy import set_printoptions
from sklearn.linear_model import LinearRegression

from pprint import pprint


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 16
rcParams['axes.titlesize'] = 20

set_printoptions(suppress=True)


# объём выборки
n = 100

x = array([ 60,  60,  60,  60,  60,  60,  60,  60,  70,  70,  70,  70,  70,
            70,  70,  70,  70,  70,  70,  70,  80,  80,  80,  70,  70,  70,
            70,  70,  70,  70,  70,  70,  70,  70,  80,  80,  80,  80,  80,
            80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,
            80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  90,  90,  90,
            80,  80,  80,  80,  90,  90,  90,  90,  90,  90,  90,  90,  90,
            90,  90,  90,  90, 100, 100,  90,  90,  90,  90, 100, 100, 100,
           100, 100, 100, 100, 100, 100, 100, 100, 100])

y = array([25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
           30, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
           35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35,
           35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 40, 40, 40,
           40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 45,
           45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 50, 50])

x_mean = x.mean()
y_mean = y.mean()

model = LinearRegression()
model.fit(x.reshape(-1, 1), y.reshape(-1, 1))

slope = model.coef_[0,0]
intercept = model.intercept_[0]

# точечный график пар значений случайных величин X и Y
plt.scatter(x, y, s=7**2)

# центр рассеивания
plt.scatter(x_mean, y_mean, s=6.5**2, c='0')
plt.annotate('A', (x_mean, y_mean), (x_mean-1, y_mean+0.5))

# теоретическая линия регрессии
plt.axline((x_mean, y_mean), slope=slope, c='0')

# запуск GUI для отображения графиков
plt.show()
