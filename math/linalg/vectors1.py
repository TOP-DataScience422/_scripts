from numpy import array


x_list_flat = [1, 4, 5, 6]
x_arr_flat = array([1, 4, 5, 6])

# >>> len(x_list_flat)
# 4
# >>>
# >>> len(x_arr_flat)
# 4
# >>>
# >>> type(x_arr_flat)
# <class 'numpy.ndarray'>
# >>>
# >>> x_arr_flat.shape
# (4,)

# ndarray — n-dimensional array — многомерный массив

x_list_orient = [
    [1],
    [4],
    [5],
    [6],
]
x_arr_orient = array([
    [1],
    [4],
    [5],
    [6],
])

# >>> len(x_list_orient)
# 4
# >>>
# >>> len(x_arr_orient)
# 4
# >>>
# >>> x_arr_orient.shape
# (4, 1)


y = array([[.3], [-7]])
z = array([[1, 4, 5, 6]])

# >>> len(z)
# 1
# >>> z.shape
# (1, 4)


# >>> y[0]
# array([0.3])
# >>>
# >>> y[1]
# array([-7.])
# >>>
# >>> y[2]
# IndexError: index 2 is out of bounds for axis 0 with size 2
# >>>
# >>> y[0][0]
# np.float64(0.3)
# >>>
# >>> y[1][0]
# np.float64(-7.0)
# >>>
# >>>
# >>> z[0]
# array([1, 4, 5, 6])
# >>>
# >>> z[1]
# IndexError: index 1 is out of bounds for axis 0 with size 1
# >>>
# >>> z[0][0]
# np.int64(1)
# >>>
# >>> z[0][1]
# np.int64(4)


# >>> for row in y:
# ...     print(row, type(row))
# ...
# [0.3] <class 'numpy.ndarray'>
# [-7.] <class 'numpy.ndarray'>
# >>>
# >>> for row in y:
# ...     for n in row:
# ...         print(n, type(n))
# ...
# 0.3 <class 'numpy.float64'>
# -7.0 <class 'numpy.float64'>
# >>>
# >>> list(y)
# [array([0.3]), array([-7.])]
# >>>
# >>> [n for row in y for n in row]
# [np.float64(0.3), np.float64(-7.0)]
# >>>
# >>> y.flat
# <numpy.flatiter object at 0x000001999F8DB9A0>
# >>>
# >>> list(y.flat)
# [np.float64(0.3), np.float64(-7.0)]
# >>>
# >>> y.flatten()
# array([ 0.3, -7. ])

