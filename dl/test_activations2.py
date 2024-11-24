from numpy import linspace

import activations as af
import neuron3 as model


x = linspace(-4, 5, 16)

dense_layers = (
    model.NeuronLayer(5, af.relu),
    model.NeuronLayer(3, af.step),
)

# breakpoint()

res = x
for layer in dense_layers:
    res = layer.out(res)


print(f'\n{x = !s}\n\n{res = !s}\n')

