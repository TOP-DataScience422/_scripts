from numpy import array, dot

from typing import Callable


class Neuron(list):
    """
    Модель нейрона для полносвязного слоя. Входы (веса) формируются динамически в момент первого выполнения линейного преобразования. На вход принимает только тензор 1-го ранга (веектор).
    """
    _default_weight = 1
    
    def __init__(self, activation_function: Callable, **params):
        self._af = activation_function
        self._af_params = params
    
    def _create_inputs(self, n=2):
        for _ in range(n):
            self.append(self._default_weight)
    
    def _linear(self, x: list):
        try:
            return dot(x, self)
        except ValueError:
            self._create_inputs(len(x))
            return dot(x, self)
    
    def _non_linear(self, x: float):
        return self._af(x, **self._af_params)
    
    def out(self, x: list):
        return self._non_linear(self._linear(x))


class NeuronLayer(list):
    """
    Модель полносвязного слоя нейронов. Не понижает ранг входного тензора.
    """
    def __init__(self, n, /, activation_function: Callable, **params):
        for _ in range(n):
            self.append(Neuron(activation_function, **params))
    
    def out(self, x: list):
        return array([
            neuron.out(x)
            for neuron in self
        ])

