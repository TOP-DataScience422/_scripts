from numpy.random import default_rng
from scipy.linalg import lu


m, n = 3, 3

A = default_rng().integers(-9, 10, size=(m,n))
P, L, U = lu(A)

# >>> P
# array([[0., 0., 1.],
#        [0., 1., 0.],
#        [1., 0., 0.]])
# >>> L
# array([[ 1.        ,  0.        ,  0.        ],
#        [-0.875     ,  1.        ,  0.        ],
#        [-0.25      ,  0.60465116,  1.        ]])
# >>> U
# array([[ -8.        ,  -2.        ,   6.        ],
#        [  0.        , -10.75      ,  -3.75      ],
#        [  0.        ,   0.        ,  -4.23255814]])

# >>> A == P @ L @ U
# array([[ True,  True,  True],
#        [ True,  True,  True],
#        [ True,  True,  True]])

