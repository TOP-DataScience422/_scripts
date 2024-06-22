from numpy import array
from numpy.linalg import norm


x = array([[3], [4], [5]])
x_T = x.T
x_flat = x.flatten()

# >>> x
# array([[3],
#        [4],
#        [5]])
# >>>
# >>> x_T
# array([[3, 4, 5]])
# >>>
# >>> x_flat
# array([3, 4, 5])


# >>> norm(x)
# np.float64(7.0710678118654755)
# >>>
# >>> norm(x_T)
# np.float64(7.0710678118654755)
# >>>
# >>> norm(x_flat)
# np.float64(7.0710678118654755)
# >>>
# >>> norm(x) == norm(x_T) == norm(x_flat)
# np.True_
# >>> 
# >>> sum(n**2 for n in x.flat)**0.5
# np.float64(7.0710678118654755)


# >>> x
# array([[3],
#        [4],
#        [5]])
# >>>
# >>> norm(x)
# np.float64(7.0710678118654755)
# >>>
# >>> 1/norm(x)
# np.float64(0.1414213562373095)
# >>>
# >>> x_unit = 1/norm(x) * x
# >>> x_unit
# array([[0.42426407],
       # [0.56568542],
       # [0.70710678]])
# >>>
# >>> norm(x_unit)
# np.float64(0.9999999999999999)
# >>>
# >>> norm(x_unit).round()
# np.float64(1.0)

