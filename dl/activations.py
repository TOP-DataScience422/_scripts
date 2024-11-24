"""
Пользовательские реализации функций активации.
"""

from math import exp


def step(x, cutoff=0):
    """Функция Хэвисайда (ступенчатая).
    
    :param cutoff: порог активации
    """
    if x <= cutoff:
        return 0
    else:
        return 1


# one hot encoding
#   класс 1 — [1 0 0 0 0]
#   класс 2 — [0 1 0 0 0]
#   класс 3 — [0 0 1 0 0]
#   класс 4 — [0 0 0 1 0]
#   класс 5 — [0 0 0 0 1]


def linear(x, slope=1, bias=0):
    """Линейная функция.
    
    :param slope: наклон
    :param bias: смещение
    """
    return slope*x + bias


def relu(x, cutoff=0, slope=1, bias=0):
    """Полулинейная функция.
    
    :param cutoff: порог активации
    :param slope: наклон
    :param bias: смещение
    """
    if x <= cutoff:
        return 0
    else:
        return slope*x + bias


def lrelu(x, cutoff=0, slope1=1, bias1=0, slope0=0.1, bias0=0):
    """Полулинейная функция c "утечкой".
    
    :param cutoff: порог активации
    :param slope1: наклон после порога
    :param bias1: смещение после 
    :param slope0: наклон до порога
    :param bias0: смещение до порога
    """
    if x <= cutoff:
        return slope0*x + bias0
    else:
        return slope1*x + bias1


def prelu(x, cutoff1=-1, cutoff2=1):
    """Кусочно-линейная функция (параметризованная полулинейная).
    
    :param x: входное значение из нормализованного ряда
    :param cutoff1: левый порог активации
    :param cutoff2: правый порог активации
    """
    if x <= cutoff1:
        return 0
    
    elif cutoff2 <= x:
        return 1
    
    else:
        slope = 1 / (cutoff2 - cutoff1)
        bias = slope * abs(cutoff1)
        return slope*x + bias


def sigmoid(x, a=1):
    """Логистическая (сигмоидальная) функция.
    
    :param a: параметр
    """
    return 1 / (1 + exp(-a*x))


def tanh(x, a=1):
    """Функция гиперболического тангенса.
    
    :param a: параметр
    """
    return 2 / (1 + exp(-2*a*x)) - 1

