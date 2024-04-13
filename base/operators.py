# операторы для работы с типом int
# >>> 1 + 2
# 3
# >>> 5 - 7
# -2
# >>> 3 * 6
# 18
# >>> 10 / 6
# 1.6666666666666667
# >>> 20 / 2
# 10.0
# >>> 10 // 6
# 1
# >>> 13 // 12
# 1
# >>> 10 % 6
# 4
# >>> 8 % 2
# 0
# >>> 2 ** 8
# 256


# операторы для работы с типом float
# >>> 1 + 2.0
# 3.0
# >>> 5 - 7.0
# -2.0
# >>> 10.0 // 6
# 1.0
# >>> 10 % 6.0
# 4.0


# операторы для работы с последовательностями
# >>> 'abc' + 'def'
# 'abcdef'
# >>>
# >>> [1, 2] + [-1, -2]
# [1, 2, -1, -2]
# >>>
# >>> 'abc' * 3
# 'abcabcabc'
# >>>
# >>> [0] * 8
# [0, 0, 0, 0, 0, 0, 0, 0]
# >>>
# >>>
# >>> 'abc' * 3.0
# TypeError: can't multiply sequence by non-int of type 'float'
# >>>
# >>> 'abc' + [1, 2]
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "list") to str
# >>>
# >>> range(5) + range(5, 10)
# TypeError: unsupported operand type(s) for +: 'range' and 'range'


# сравнительные операторы
# >>> 1 == 1
# True
# >>> 1 == 2
# False
# >>>
# >>> 3 != 4
# True
# >>> 3 != 3
# False
# >>>
# >>> 4 > 3
# True
# >>> 4 > 5
# False
# >>> 4 > 4
# False
# >>>
# >>> 4 >= 3
# True
# >>> 4 >= 5
# False
# >>> 4 >= 4
# True


# сравнение последовательностей
# >>> 'abc' == 'ABC'
# False
# >>>
# >>> ord('b')
# 98
# >>> ord('B')
# 66
# >>>
# >>> 'z' == 'zz'
# False
# >>>
# >>> 'abc' > 'aaa'
# True
# >>>
# >>> ord('a')
# 97
# >>> ord('b')
# 98
# >>>
# >>> 'abc' > 'aaz'
# True
# >>>
# >>> 'a' < 'aaa'
# True
# >>>
# >>> 'ab' > 'aazz'
# True
# >>>
# >>> '9' < '12'
# False
# >>>
# >>> ord('9')
# 57
# >>> ord('1')
# 49
# >>>
# >>> [1, 2, 3] < [4, 5, 6]
# True
# >>>
# >>> (1, 2, 3) < (4, 5, 6)
# True
# >>>
# >>> ('ab', 'cd') < (10, 20)
# TypeError: '<' not supported between instances of 'str' and 'int'


# условный оператор
# >>> 10 if True else -10
# 10
# >>> 10 if False else -10
# -10

