# def <идентификатор>([<параметр> [, <параметр>]]):
#     <тело_функции>
#     ...


def first_function():
    print('hello world from function')


first_function()

# >>> first_function
# <function first_function at 0x00000266569A8A40>
# >>>
# >>> type(first_function)
# <class 'function'>

# >>> first_function.__name__
# 'first_function'
# >>>
# >>> var = first_function
# >>> var.__name__
# 'first_function'
# >>>
# >>> var()
# hello world from function

