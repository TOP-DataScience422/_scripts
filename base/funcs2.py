def adder1():
    print(5 + 6)


def adder2():
    return 5 + 6


# >>> adder1
# <function adder1 at 0x0000024FE83F8A40>
# >>>
# >>> adder2
# <function adder2 at 0x0000024FE881EFC0>
# >>>
# >>>
# >>> adder1()
# 11
# >>> adder2()
# 11
# >>>
# >>> n1 = adder1()
# 11
# >>> n2 = adder2()
# >>>
# >>> n1
# >>> n2
# 11
# >>>
# >>> type(n1)
# <class 'NoneType'>
# >>>
# >>> type(n2)
# <class 'int'>


def two_divisors():
    n = 18
    result = []
    for d in range(1, n+1):
        print(f'{d = }')
        if n % d == 0:
            result.append(d)
        if len(result) > 1:
            return result


# >>> two_divisors()
# d = 1
# d = 2
# [1, 2]


def geometry():
    shape = input('введите название плоской фигуры: ')
    if shape == 'отрезок':
        return '—' * 40
    elif shape == 'квадрат':
        line = '—' * 10
        sides = f'|{" "*8}|'
        return f'{line}\n{"\n".join([sides]*4)}\n{line}'


# >>> geometry()
# введите название плоской фигуры: отрезок
# '————————————————————————————————————————'
# >>>
# >>> square = geometry()
# введите название плоской фигуры: квадрат
# >>>
# >>> square
# '——————————\n|        |\n|        |\n|        |\n|        |\n——————————'
# >>>
# >>> print(square)
# ——————————
# |        |
# |        |
# |        |
# |        |
# ——————————

