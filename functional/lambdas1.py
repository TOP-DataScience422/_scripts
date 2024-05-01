func1 = lambda: print('вызов')
func2 = lambda n1, n2, d=3: round((n1 + n2) / 2, d)

# >>> func1
# <function <lambda> at 0x0000022D45EF8A40>
# >>>
# >>> func2
# <function <lambda> at 0x0000022D4631EFC0>
# >>>
# >>> type(func1)
# <class 'function'>
# >>>
# >>> type(func2)
# <class 'function'>
# >>>
# >>> func1()
# вызов
# >>>
# >>> func2(3, 5)
# 4.0
# >>>
# >>> func1.__name__
# '<lambda>'
# >>>
# >>> func2.__name__
# '<lambda>'

