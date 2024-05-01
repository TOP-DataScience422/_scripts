def decorator(func_obj: 'function') -> 'function':
    print('начало вызова функции-декоратора')
    
    def wrapper(*args, **kwargs) -> 'any':
        """Функция-обёртка."""
        print('начало вызова функции-обёртки')
        result = func_obj(*args, **kwargs)
        print('конец вызова функции-обёртки')
        return result
    
    print('конец вызова функции-декоратора')
    return wrapper


def test_function():
    """Функция для теста декоратора."""
    print('вызов декорируемой функции')


# >>> test_function
# <function test_function at 0x000001CA20DBEFC0>
# >>>
# >>> type(test_function)
# <class 'function'>
# >>>
# >>> test_function.__name__
# 'test_function'
# >>>
# >>> test_function.__doc__
# 'Функция для теста декоратора.'
# >>>
# >>> test_function()
# вызов декорируемой функции

# >>> test_function = decorator(test_function)
# начало вызова функции-декоратора
# конец вызова функции-декоратора
# >>>
# >>> test_function
# <function decorator.<locals>.wrapper at 0x000001CA20DBF060>
# >>>
# >>> type(test_function)
# <class 'function'>
# >>>
# >>> test_function.__name__
# 'wrapper'
# >>>
# >>> test_function.__doc__
# 'Функция-обёртка.'
# >>>
# >>> test_function()
# начало вызова функции-обёртки
# вызов декорируемой функции
# конец вызова функции-обёртки


# >>> len
# <built-in function len>
# >>>
# >>> type(len)
# <class 'builtin_function_or_method'>
# >>>
# >>> var = len([1, 2, 3])
# >>> var
# 3

# >>> len = decorator(len)
# начало вызова функции-декоратора
# конец вызова функции-декоратора
# >>>
# >>> len
# <function decorator.<locals>.wrapper at 0x0000024772CFF1A0>
# >>>
# >>> type(len)
# <class 'function'>
# >>>
# >>> var = len([1, 2, 3])
# начало вызова функции-обёртки
# конец вызова функции-обёртки
# >>> var
# 3


@decorator
def test_function_2(name: str):
    print(f'привет, {name}')


# начало вызова функции-декоратора
# конец вызова функции-декоратора
# >>>
# >>> test_function_2
# <function decorator.<locals>.wrapper at 0x000001A7B18FF100>
# >>>
# >>> test_function_2('Геннадий')
# начало вызова функции-обёртки
# привет, Геннадий
# конец вызова функции-обёртки

