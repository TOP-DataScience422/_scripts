from numpy import array, dot


x = array([-0.1, 0.2])
p_x = array([2/3, 1/3])
m_x = dot(x, p_x)

y = array([-100, 100])
p_y = array([.5, .5])
m_y = dot(y, p_y)

# >>> m_x == m_y
# np.True_

d1_x = sum(
    (x[i] - m_x)**2 * p_x[i] 
    for i in range(len(x))
)
# >>> d1_x
# np.float64(0.020000000000000004)

d2_x = dot(x**2, p_x) - m_x**2

# >>> d1_x == d2_x
# np.True_

d_y = dot(y**2, p_y) - m_y**2
# >>> d_y
# np.float64(10000.0)

sigma_x = d1_x**0.5
# >>> sigma_x
# np.float64(0.14142135623730953)

sigma_y = d_y**0.5
# >>> sigma_y
# np.float64(100.0)


x_norm = (x - m_x) / sigma_x

# >>> array([x_norm, p_x])
# array([[-0.70710678,  1.41421356],
#        [ 0.66666667,  0.33333333]])

y_norm = (y - m_y) / sigma_y

# >>> array([y_norm, p_y])
# array([[-1. ,  1. ],
#        [ 0.5,  0.5]])

