from numpy import array
from numpy.linalg import matrix_rank, inv
from numpy.random import default_rng


# x + y = 4
# –x/2 + y = 2

A = array([
    [1, 1],
    [-0.5, 1],
])
b = array([4, 2]).reshape(2, 1)

# >>> matrix_rank(A)
# np.int64(2)
# >>>
# >>> inv(A)
# array([[ 0.66666667, -0.66666667],
#        [ 0.33333333,  0.66666667]])
# >>>
# >>> b @ inv(A)
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 1)
# >>>
# >>> inv(A) @ b
# array([[1.33333333],
#        [2.66666667]])
# >>>
# >>> x, y = (inv(A) @ b).flat
# >>>
# >>> print(f'{x = !s}\n{y = !s}')
# x = 1.3333333333333337
# y = 2.6666666666666665

