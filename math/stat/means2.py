from numpy import array, dot

from itertools import product


x = array([1, 4, 5, 7, 12, 14, 19])
p_x = array([.01, .94, .01, .01, .01, .01, .01])

y = array([2, 6, 7, 10, 11, 12, 17])
p_y = array([.01, .01, .01, .01, .01, .01, .94])

# сложение случайных величин (законов распределения)
z = [a + b for a, b in product(x, y, repeat=1)]
p_z = [a * b for a, b in product(p_x, p_y, repeat=1)]
zz = {}
for i in range(len(z)):
    zz[z[i]] = zz.get(z[i], 0) + p_z[i]
zz = dict(sorted(zz.items()))

# случайная величина z равна сумме случайных величин x и y
z = array([*zz.keys()])
p_z = array([*zz.values()])

# проверка
# >>> sum(p_z)
# np.float64(0.9999999999999998)

# >>> dot(x, p_x)
# np.float64(4.339999999999999)
# >>>
# >>> dot(y, p_y)
# np.float64(16.459999999999997)
# >>>
# >>> dot(z, p_z)
# np.float64(20.799999999999997)
# >>>
# >>> dot(x, p_x) + dot(y, p_y) == dot(z, p_z)
# np.True_

