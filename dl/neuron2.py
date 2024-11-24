from numpy import array

import neuron1


class NeuronLayer(list):
    """
    Модель простого слоя нейронов.
    
    Вход: матрица (тензор 2-го ранга)
    Выход: вектор (тензор 1-го ранга)
    """
    def __init__(self, weights):
        for w in weights.T:
            self.append(neuron1.Neuron(*w))
    
    def out(self, x):
        x = x.T
        result = []
        for i, n in enumerate(self):
            result.append(n.out(*x[i]))
        return array(result)


# подбор весов — обучение
weights = array([
    [-1, 0, 1],
    [1, 0, 0],
])
nl1 = NeuronLayer(weights)

inp = array([
    [10, 9],
    [9, 8],
    [8, 7],
]).T

