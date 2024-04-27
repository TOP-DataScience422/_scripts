def calculator(num1, num2, sign, fixed=2):
    if sign == '+':
        return round(num1 + num2, fixed)
    
    elif sign == '-':
        return round(num1 - num2, fixed)
    
    elif sign == '*':
        return round(num1 * num2, fixed)
    
    elif sign == '/':
        if num2:
            return round(num1 / num2, fixed)
        else:
            return float('inf')


# >>> calculator(1, 2, '+')
# 3
# >>> calculator(1, 7, '/')
# 0.14
# >>> calculator(1, 7, '/', 4)
# 0.1429
# >>> calculator(1, 0, '/')
# inf

# >>> calculator(num1=21, num2=7, sign='*', fixed=0)
# 147
# >>> calculator(sign='*', num2=0.5, num1=1.8, fixed=1)
# 0.9
# >>> calculator(0.95, 16.74, fixed=3, sign='*')
# 15.903
# >>> calculator(fixed=3, 0.95, 16.74, sign='*')
# SyntaxError: positional argument follows keyword argument

# >>> calculator(10, 5)
# TypeError: calculator() missing 1 required positional argument: 'sign'
# >>>
# >>> calculator(10, 5, '/', 1, 'asd')
# TypeError: calculator() takes from 3 to 4 positional arguments but 5 were given


def normalizer(value: float, scale: int) -> float:
    """Нормализует значение в рамках переданного максимального значения шкалы."""
    return value / scale


# >>> normalizer.__doc__
# 'Нормализует значение в рамках переданного максимального значения шкалы.'

# >>> normalizer.__annotations__
# {'value': <class 'float'>, 'scale': <class 'int'>, 'return': <class 'float'>}

# проверка типов не выявит несоответствие
normalizer(15, 90)
normalizer(0.2, 5)
# проверка типов выявит несоответствие
normalizer(12.1, 44.4)
normalizer(1+1j, 5.2)

