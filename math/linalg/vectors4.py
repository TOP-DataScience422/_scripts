from numpy import array, dot


v1 = array([[1, 2, 3, 4]])
v2 = array([[5, 6, 7, 8]])

v1_flat = v1.flatten()
v2_flat = v2.flatten()


# >>> sum(v1_flat[i]*v2_flat[i] for i in range(len(v1_flat)))
# np.int64(70)
# >>> 
# >>> dot(v1_flat, v2_flat)
# np.int64(70)
# >>>
# >>> dot(v1, v2)
# ValueError: shapes (1,4) and (1,4) not aligned: 4 (dim 1) != 1 (dim 0)
# >>>
# >>> dot(v1.flat, v2.flat)
# np.int64(70)


# >>> 100 * v1_flat
# array([100, 200, 300, 400])
# >>>
# >>> 0.01 * v1_flat
# array([0.01, 0.02, 0.03, 0.04])
# >>>
# >>> dot(v1_flat, v2_flat)
# np.int64(70)
# >>>
# >>> dot(100*v1_flat, v2_flat)
# np.int64(7000)
# >>>
# >>> dot(0.01*v1_flat, v2_flat)
# np.float64(0.7)


a = array([0, 1, 2])
b = array([3, 5, 8])
c = array([13, 21, 34])

res1 = dot(a, b+c)
res2 = dot(a, b) + dot(a, c)

# >>> res1
# np.int64(110)
# >>> 
# >>> res2
# np.int64(110)
# >>>
# >>> res1 == res2
# np.True_


x = array([0, 4])
y = array([4, 0])

# >>> dot(x, y)
# np.int64(0)

