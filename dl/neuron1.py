class Neuron:
    """
    Модель искусственного нейрона с двумя входами.
    
    Вход: вектор (тензор 1-го ранга)
    Выход: скаляр (тензор 0-го ранга)
    """
    def __init__(self, weight1=0, weight2=0):
        if weight1 not in (-1, 0, 1):
            weight1 = 0
        if weight2 not in (-1, 0, 1):
            weight2 = 0
        self._w1 = weight1
        self._w2 = weight2
    
    @property
    def w1(self):
        return self._w1
    
    @w1.setter
    def w1(self, value):
        if value not in (-1, 0, 1):
            return
        self._w1 = value
    
    @property
    def w2(self):
        return self._w2
    
    @w2.setter
    def w2(self, value):
        if value not in (-1, 0, 1):
            return
        self._w2 = value
    
    def _linear(self, x1, x2):
        """Линейное преобразование: сумматор."""
        return x1 * self._w1 + x2 * self._w2
    
    def _non_linear(self, x, cutoff=0):
        """Нелинейное преобразование: функция Хэвисайда (стуепнька)."""
        if x <= cutoff:
            return 0
        else:
            return 1
    
    def out(self, x1, x2):
        return self._non_linear(self._linear(x1, x2))


# выходы:
# 0 - похолодание
# 1 - потепление

# подбор весов — обучение
w1, w2 = -1, 1
weather = Neuron(w1, w2)

# >>> weather.out(1, 5)
# 1
# >>> weather.out(1, 2)
# 1
# >>> weather.out(1, -1)
# 0
# >>> weather.out(1, 0)
# 0

# >>> weather.out(10, 10)
# 0

