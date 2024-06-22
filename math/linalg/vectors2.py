from numpy import array


v1 = array([[4], [5], [6]])
v2 = array([[10], [20], [30]])
v3 = array([[1], [2], [3], [4], [5]])
v4 = array([[10, 20, 30]])

# >>> v1 + 6
# array([[10],
#        [11],
#        [12]])
# >>>
# >>> v1 - 4
# array([[0],
#        [1],
#        [2]])
# >>>
# >>> v2 * 10
# array([[100],
#        [200],
#        [300]])


# >>> v1 + v2
# array([[14],
#        [25],
#        [36]])
# >>>
# >>> v2 - v1
# array([[ 6],
#        [15],
#        [24]])

# >>> v1 + v3
# ValueError: operands could not be broadcast together with shapes (3,1) (5,1)


# >>> v1 + v4
# array([[14, 24, 34],
#        [15, 25, 35],
#        [16, 26, 36]])

v1_T = array([[4, 5, 6]])
v4_T = array([[10], [20], [30]])

# >>> v1_T + v4_T
# array([[14, 15, 16],
#        [24, 25, 26],
#        [34, 35, 36]])


# >>> v1.shape
# (3, 1)
# >>>
# >>> v1_T.shape
# (1, 3)
# >>>
# >>> v2.T
# array([[10, 20, 30]])
# >>>
# >>> v2.shape
# (3, 1)
# >>>
# >>> v2_T = v2.T
# >>>
# >>> type(v2_T)
# <class 'numpy.ndarray'>
# >>>
# >>> v2_T.shape
# (1, 3)
# >>>
# >>> v4.shape
# (1, 3)
# >>>
# >>> v4.T
# array([[10],
#        [20],
#        [30]])
# >>>
# >>> v4.T.shape
# (3, 1)


# >>> v4_T == v4.T
# array([[ True],
#        [ True],
#        [ True]])
# >>>
# >>> all(v4_T == v4.T)
# True

# >>> v4_T == v4
# array([[ True, False, False],
#        [False,  True, False],
#        [False, False,  True]])
# >>>
# >>> all(v4_T == v4)
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# >>>
# >>> (v4_T == v4).all()
# np.False_

# >>> v1 < v2
# array([[ True],
#        [ True],
#        [ True]])


