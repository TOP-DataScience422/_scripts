from numpy import array, arange, diag, tril, triu, eye, zeros
from numpy.random import default_rng


m1 = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])

# >>> type(m1)
# <class 'numpy.ndarray'>
# >>>
# >>> m1.shape
# (4, 3)

for row in m1:
    print(row, type(row), row.shape)

# [1 2 3] <class 'numpy.ndarray'> (3,)
# [4 5 6] <class 'numpy.ndarray'> (3,)
# [7 8 9] <class 'numpy.ndarray'> (3,)
# [10 11 12] <class 'numpy.ndarray'> (3,)

for row in m1:
    for n in row:
        print(n, type(n))

# 1 <class 'numpy.int64'>
# 2 <class 'numpy.int64'>
# 3 <class 'numpy.int64'>
# 4 <class 'numpy.int64'>
# 5 <class 'numpy.int64'>
# 6 <class 'numpy.int64'>
# 7 <class 'numpy.int64'>
# 8 <class 'numpy.int64'>
# 9 <class 'numpy.int64'>
# 10 <class 'numpy.int64'>
# 11 <class 'numpy.int64'>
# 12 <class 'numpy.int64'>


# >>> m1[0][0]
# np.int64(1)
# >>>
# >>> m1[0,0]
# np.int64(1)

# >>> m1[0]
# array([1, 2, 3])
# >>> 
# >>> m1[:,0]
# array([ 1,  4,  7, 10])

# >>> m1[:,:2]
# array([[ 1,  2],
#        [ 4,  5],
#        [ 7,  8],
#        [10, 11]])
# >>>
# >>> m1[2:,1:]
# array([[ 8,  9],
#        [11, 12]])
# >>>
# >>> m1[::2,::2]
# array([[1, 3],
#        [7, 9]])


# >>> m1.diagonal()
# array([1, 5, 9])
# >>> 
# >>> n, k = m1.shape
# >>> array([m1[i,k-i-1] for i in range(k)])
# array([3, 5, 7])


# >>> m1.reshape(2, 6)
# array([[ 1,  2,  3,  4,  5,  6],
#        [ 7,  8,  9, 10, 11, 12]])
# >>>
# >>> array(range(1, 101)).reshape(10, 10)
# array([[  1,   2,   3,   4,   5,   6,   7,   8,   9,  10],
#        [ 11,  12,  13,  14,  15,  16,  17,  18,  19,  20],
#        [ 21,  22,  23,  24,  25,  26,  27,  28,  29,  30],
#        [ 31,  32,  33,  34,  35,  36,  37,  38,  39,  40],
#        [ 41,  42,  43,  44,  45,  46,  47,  48,  49,  50],
#        [ 51,  52,  53,  54,  55,  56,  57,  58,  59,  60],
#        [ 61,  62,  63,  64,  65,  66,  67,  68,  69,  70],
#        [ 71,  72,  73,  74,  75,  76,  77,  78,  79,  80],
#        [ 81,  82,  83,  84,  85,  86,  87,  88,  89,  90],
#        [ 91,  92,  93,  94,  95,  96,  97,  98,  99, 100]])
# >>> 
# >>> default_rng().integers(low=0, high=10, size=24).reshape(4, 6)
# array([[1, 4, 0, 1, 6, 6],
#        [6, 5, 9, 5, 8, 4],
#        [4, 8, 6, 9, 7, 1],
#        [4, 7, 9, 9, 3, 5]])


# >>> arange(1, 10)
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>>
# >>> diag(arange(1, 10))
# array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 2, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 3, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 4, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 5, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 6, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 7, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 8, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 9]])


m2 = default_rng().integers(low=0, high=10, size=(4, 4))

# >>> m2
# array([[3, 7, 8, 7],
#        [8, 6, 8, 3],
#        [8, 5, 6, 6],
#        [6, 1, 6, 8]])
# >>>
# >>> tril(m2)
# array([[3, 0, 0, 0],
#        [8, 6, 0, 0],
#        [8, 5, 6, 0],
#        [6, 1, 6, 8]])
# >>>
# >>> triu(m2)
# array([[3, 7, 8, 7],
#        [0, 6, 8, 3],
#        [0, 0, 6, 6],
#        [0, 0, 0, 8]])


# >>> eye(4, dtype=int)
# array([[1, 0, 0, 0],
#        [0, 1, 0, 0],
#        [0, 0, 1, 0],
#        [0, 0, 0, 1]])


# >>> zeros((4, 4), dtype=int)
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]])

