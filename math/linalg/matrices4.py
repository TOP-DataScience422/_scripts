from numpy import array, eye, diag
from numpy.linalg import matrix_rank, null_space
from numpy.random import default_rng


m1 = default_rng().integers(0, 10, size=(2, 2))
m2 = default_rng().integers(0, 10, size=(3, 3))
m3 = array([
    [1, 2, 4],
    [2, 4, 8],
    [3, 6, 12],
])

# >>> print(m1)
# [[8 6]
#  [1 9]]
# >>>
# >>> print(m2)
# [[1 0 3]
#  [6 7 9]
#  [8 0 5]]
# >>>
# >>> print(m3)
# [[ 1  2  4]
#  [ 2  4  8]
#  [ 3  6 12]]


# >>> null_space(m1)
# array([], shape=(2, 0), dtype=float64)
# >>>
# >>> m1.T
# array([[8, 1],
#        [6, 9]])
# >>>
# >>> null_space(m1.T)
# array([], shape=(2, 0), dtype=float64)
# >>>
# >>> matrix_rank(m1)
# np.int64(2)


# >>> null_space(m2)
# array([], shape=(3, 0), dtype=float64)
# >>>
# >>> m2.T
# array([[1, 6, 8],
#        [0, 7, 0],
#        [3, 9, 5]])
# >>>
# >>> null_space(m2.T)
# array([], shape=(3, 0), dtype=float64)
# >>>
# >>> matrix_rank(m2)
# np.int64(3)


# >>> null_space(m3)
# array([[-0.97590007, -0.        ],
#        [ 0.09759001,  0.89442719],
#        [ 0.19518001, -0.4472136 ]])
# >>>
# >>> m3.T
# array([[ 1,  2,  3],
#        [ 2,  4,  6],
#        [ 4,  8, 12]])
# >>>
# >>> null_space(m3.T)
# array([[ 0.57735027,  0.77151675],
#        [ 0.57735027, -0.6172134 ],
#        [-0.57735027,  0.15430335]])
# >>>
# >>> matrix_rank(m3)
# np.int64(1)


# >>> print(eye(2, dtype=int))
# [[1 0]
#  [0 1]]
# >>>
# >>> matrix_rank(eye(2, dtype=int))
# np.int64(2)
# >>>
# >>>
# >>> print(eye(5, dtype=int))
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]
# >>>
# >>> matrix_rank(eye(5, dtype=int))
# np.int64(5)


m4 = diag(default_rng().integers(-5, 6, size=4))

# >>> print(m4)
# [[-3  0  0  0]
#  [ 0 -4  0  0]
#  [ 0  0  4  0]
#  [ 0  0  0  3]]
# >>>
# >>> matrix_rank(m4)
# np.int64(4)
# >>>
# >>> m4[1,1] = 0
# >>> print(m4)
# [[-3  0  0  0]
#  [ 0  0  0  0]
#  [ 0  0  4  0]
#  [ 0  0  0  3]]
# >>>
# >>> matrix_rank(m4)
# np.int64(3)


