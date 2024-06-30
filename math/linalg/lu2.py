from numpy import array, eye, concat
from numpy.random import default_rng
from sympy import Matrix


m, n = 2, 2

m1 = default_rng().integers(-9, 10, size=(m,n))
I2 = eye(2, dtype=int)

m1_I2 = concat([m1, I2], axis=1)
m1_I2_rref = array(
    Matrix(m1_I2).rref()[0], 
    dtype=float
)
m1_inv = m1_I2_rref[:,2:]

# >>> m1_I2_rref
# array([[ 1.        ,  0.        ,  0.02631579,  0.10526316],
#        [ 0.        ,  1.        ,  0.23684211, -0.05263158]])
# >>>
# >>> m1 @ m1_inv
# array([[1., 0.],
#        [0., 1.]])

