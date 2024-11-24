from matplotlib import pyplot as plt
from numpy import linspace, array
from pandas import DataFrame, option_context

import activations as af


x1 = linspace(-2, 9, 100)
x1_norm = (x1 - x1.mean()) / x1.std()

y1_step = array([af.step(xi) for xi in x1])
y1_lin = array([af.linear(xi) for xi in x1])
y1_relu = array([af.relu(xi) for xi in x1])
y1_lrelu = array([af.lrelu(xi) for xi in x1])
y1_prelu = array([af.prelu(xi) for xi in x1_norm])
y1_sigm = array([af.sigmoid(xi) for xi in x1_norm])
y1_tanh = array([af.tanh(xi) for xi in x1_norm])

test1 = DataFrame({
    'x1': x1, 
    'step': y1_step,
    'lin': y1_lin,
    'relu': y1_relu,
    'lrelu': y1_lrelu
})
test1_norm = DataFrame({
    'x1_norm': x1_norm, 
    'prelu': y1_prelu,
    'sigm': y1_sigm,
    'tanh': y1_tanh,
})

print()
with option_context('display.max_rows', None):
    print(test1.round(1), end='\n\n')
with option_context('display.max_rows', None):
    print(test1_norm.round(3), end='\n\n')


fig = plt.figure(figsize=(12, 5))
axs = fig.subplots(2, 4)

axs[0][0].plot(x1, y1_step)
axs[0][0].set(title='step')

axs[0][1].plot(x1, y1_lin)
axs[0][1].set(title='lin')

axs[0][2].plot(x1, y1_relu)
axs[0][2].set(title='relu')

axs[0][3].plot(x1, y1_lrelu)
axs[0][3].set(title='lrelu')

axs[1][0].plot(x1_norm, y1_prelu)
axs[1][0].set(title='prelu')

axs[1][1].plot(x1_norm, y1_sigm)
axs[1][1].set(title='sigm')

axs[1][2].plot(x1_norm, y1_tanh)
axs[1][2].set(title='tanh')

plt.show()

