# >>> t1 = (12, 1, 2, 3, 10)
# >>>
# >>> type(t1)
# <class 'tuple'>
# >>>
# >>> print(t1)
# (12, 1, 2, 3, 10)
# >>>
# >>> print(*t1)
# 12 1 2 3 10
# >>>
# >>> print(t1[0], t1[1], t1[2], t1[3], t1[4])
# 12 1 2 3 10
# >>>
# >>> print(*t1, sep=' # ')
# 12 # 1 # 2 # 3 # 10
# >>>
# >>> print(*t1, sep='\n')
# 12
# 1
# 2
# 3
# 10
# >>>
# >>> range(*t1)
# TypeError: range expected at most 3 arguments, got 5
# >>>
# >>> l1 = [10, 20]
# >>>
# >>> range(*l1)
# range(10, 20)
# >>>
# >>> range(l1[0], l1[1])
# range(10, 20)


# >>> a, b = l1
# >>> a
# 10
# >>> b
# 20
# >>>
# >>> a, b = [1, 2, 3]
# ValueError: too many values to unpack (expected 2)
# >>>
# >>> a, b, c, d = [1, 2, 3]
# ValueError: not enough values to unpack (expected 4, got 3)


# >>> ranges = [
# ...   (1, 10),
# ...   (2, 8),
# ...   (-15, -10),
# ... ]
# >>> for item in ranges:
# ...     print(type(item), item)
# ...
# <class 'tuple'> (1, 10)
# <class 'tuple'> (2, 8)
# <class 'tuple'> (-15, -10)
# >>>
# >>> for item in ranges:
# ...     print(item[0], item[1], sep='\t')
# ...
# 1       10
# 2       8
# -15     -10
# >>>
# >>> for l, r in ranges:
# ...     print(l, r, sep='\t')
# ...
# 1       10
# 2       8
# -15     -10

