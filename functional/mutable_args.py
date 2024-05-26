def func(arg: list | dict | set):
    print(id(arg))
    arg.clear()


l1 = [1, 2, 3]
d1 = {'a': .1, 'b': .2}
s1 = {'1', '2', '3'}

# >>> id(l1)
# 2617069131968
# >>> id(d1)
# 2617071203904
# >>> id(s1)
# 2617071220128
# >>>
# >>> func(l1)
# 2617069131968
# >>> func(d1)
# 2617071203904
# >>> func(s1)
# 2617071220128
# >>>
# >>> l1
# []
# >>> d1
# {}
# >>> s1
# set()

