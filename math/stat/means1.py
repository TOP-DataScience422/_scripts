from numpy import array, mean, dot, average, median
from numpy import set_printoptions
from numpy.ma import sort


set_printoptions(suppress=True)

x = array([ 1,   4,   5,   7,  12,  14,  19])
p1 = array([.01, .94, .01, .01, .01, .01, .01])
p2 = array([.01, .01, .01, .01, .01, .01, .94])

# сумма вероятностей
# >>> sum(p1)
# np.float64(1.0)

# среднее арифметическое
# >>> sum(x) / len(x)
# np.float64(8.857142857142858)
# >>>
# >>> mean(x)
# np.float64(8.857142857142858)

# законы распределения
# >>> array([x, p1])
# array([[ 1.  ,  4.  ,  5.  ,  7.  , 12.  , 14.  , 19.  ],
#        [ 0.01,  0.94,  0.01,  0.01,  0.01,  0.01,  0.01]])
# >>>
# >>> array([x, p2])
# array([[ 1.  ,  4.  ,  5.  ,  7.  , 12.  , 14.  , 19.  ],
#        [ 0.01,  0.01,  0.01,  0.01,  0.01,  0.01,  0.94]])

# математическое ожидание
# >>> sum(x[i]*p1[i] for i in range(len(x)))
# np.float64(4.339999999999999)
# >>>
# >>> dot(x, p1)
# np.float64(4.339999999999999)
# >>>
# >>> dot(x, p2)
# np.float64(18.29)

# >>> array([x*10, p2])
# array([[ 10.  ,  40.  ,  50.  ,  70.  , 120.  , 140.  , 190.  ],
#        [  0.01,   0.01,   0.01,   0.01,   0.01,   0.01,   0.94]])
# >>>
# >>> dot(x*10, p2)
# np.float64(182.9)
# >>>
# >>> 10 * dot(x, p2)
# np.float64(182.89999999999998)


x3_sample = array([38, 39, 40, 38, 39, 41, 40, 42, 38, 45])

x3 = array([38, 39, 40, 41, 42, 45])
w3 = array([.3, .2, .2, .1, .1, .1])

# среднее взвешенное
# >>> average(x3, weights=w3)
# np.float64(40.000000000000014)
# >>>
# >>> dot(x3, w3)
# np.float64(40.00000000000001)


# медиана
# >>> sort(x3_sample)
# array([38, 38, 38, 39, 39, 40, 40, 41, 42, 45])
# >>> 
# >>> h = len(x3_sample)
# >>> 
# >>> (sort(x3_sample)[h//2-1] + sort(x3_sample)[h//2]) / 2
# np.float64(39.5)
# >>> 
# >>> median(x3_sample)
# np.float64(39.5)

# >>> median(x3)
# np.float64(40.5)

