from numpy import array, dot


t = array([3, 3])
r = array([7, 2])

t_coll = dot(t, r) / dot(r, r) * r
t_orth = t - t_coll

# >>> t_coll
# array([3.56603774, 1.01886792])
# >>>
# >>> t_orth
# array([-0.56603774,  1.98113208])

# >>> dot(t_coll, t_orth)
# np.float64(4.440892098500626e-16)
# >>>
# >>> dot(t_orth, r)
# np.float64(8.881784197001252e-16)

