from numpy import array, zeros, eye, dot
from numpy.random import default_rng


z = zeros((4, 4), dtype=int)
I = eye(4, dtype=int)

# >>> z
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]])
# >>>
# >>> z + 5
# array([[5, 5, 5, 5],
#        [5, 5, 5, 5],
#        [5, 5, 5, 5],
#        [5, 5, 5, 5]])
# >>>
# >>> I
# array([[1, 0, 0, 0],
#        [0, 1, 0, 0],
#        [0, 0, 1, 0],
#        [0, 0, 0, 1]])
# >>>
# >>> z+5 + I
# array([[6, 5, 5, 5],
#        [5, 6, 5, 5],
#        [5, 5, 6, 5],
#        [5, 5, 5, 6]])


m1 = default_rng().integers(low=0, high=10, size=(3, 2))
m2 = default_rng().integers(low=0, high=10, size=(3, 2))

# >>> m1
# array([[7, 2],
#        [8, 1],
#        [7, 2]])
# >>>
# >>> m2
# array([[3, 2],
#        [1, 1],
#        [5, 0]])


# >>> m1 * m2
# array([[21,  4],
#        [ 8,  1],
#        [35,  0]])


m3 = default_rng().integers(low=0, high=10, size=(2, 3))
m4 = default_rng().integers(low=0, high=10, size=(3, 2))

# >>> m3
# array([[3, 1, 1],
#        [1, 7, 8]])
# >>>
# >>> m4
# array([[2, 9],
#        [5, 6],
#        [9, 6]])

# >>> M, N1 = m3.shape
# >>> N2, K = m4.shape
# >>>
# >>> N1 == N2
# True
# >>>
# >>> M, K
# (2, 2)

# >>> dot(m3[0], m4[:,0])
# np.int64(20)
# >>>
# >>> dot(m3[0], m4[:,1])
# np.int64(39)
# >>>
# >>> dot(m3[1], m4[:,0])
# np.int64(109)
# >>>
# >>> dot(m3[1], m4[:,1])
# np.int64(99)

# >>> m3 @ m4
# array([[ 20,  39],
#        [109,  99]])
# >>>
# >>> dot(m3, m4)
# array([[ 20,  39],
#        [109,  99]])

v1 = array([
    [2],
    [2],
    [2],
])

# >>> m1.shape, v1.shape
# ((3, 2), (3, 1))
# >>>
# >>> m2.shape, v1.shape
# ((3, 2), (3, 1))
# >>>
# >>> m3.shape, v1.shape
# ((2, 3), (3, 1))
# >>>
# >>> m4.shape, v1.shape
# ((3, 2), (3, 1))

# >>> m3 @ v1
# array([[10],
#        [32]])

