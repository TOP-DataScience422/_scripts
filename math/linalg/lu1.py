from numpy import array, eye, concat
from numpy.random import default_rng
from sympy import Matrix


m, n = 3, 3

m1 = default_rng().integers(-9, 10, size=(m,n))
I3 = eye(3, dtype=int)

m1_ex = concat([m1, I3[:,0].reshape(3, 1)], axis=1)
m1_rref = array(Matrix(m1_ex).rref()[0], dtype=float)

print(m1, m1_ex, m1_rref, sep='\n\n')

#[[ 7  3 -9]
# [ 8 -9  8]
# [ 8 -9  6]]
#
#[[ 7  3 -9  1]
# [ 8 -9  8  0]
# [ 8 -9  6  0]]
#
#[[1.         0.         0.         0.10344828]
# [0.         1.         0.         0.09195402]
# [0.         0.         1.         0.        ]]

