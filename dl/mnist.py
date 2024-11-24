# добавить TF_ENABLE_ONEDNN_OPTS=0 в качестве системной переменной окружения или использовать:
# import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# прописать в начале файла ...\site-packages\keras\src\utils\progbar.py
# import colorama
# colorama.init()

from pathlib import Path
from sys import path

from matplotlib import pyplot as plt
from numpy import load as np_load

from keras import Input
from keras.layers import Dense
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy 
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical


digits_imgs = np_load(Path(path[0]) / 'mnist.npz')

x_train = digits_imgs['x_train']
y_train = digits_imgs['y_train']
x_test = digits_imgs['x_test']
y_test = digits_imgs['y_test']

# print(y_train[0])
# plt.imshow(x_train[0], cmap='gray')
# plt.show()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

x_train = x_train / 255
x_test = x_test / 255

# one hot encoding
#   0 -> [1 0 0 0 0 0 0 0 0 0]
#   1 -> [0 1 0 0 0 0 0 0 0 0]
#   2 -> [0 0 1 0 0 0 0 0 0 0]
#   3 -> [0 0 0 1 0 0 0 0 0 0]
#   4 -> [0 0 0 0 1 0 0 0 0 0]
#   5 -> [0 0 0 0 0 1 0 0 0 0]
#   6 -> [0 0 0 0 0 0 1 0 0 0]
#   7 -> [0 0 0 0 0 0 0 1 0 0]
#   8 -> [0 0 0 0 0 0 0 0 1 0]
#   9 -> [0 0 0 0 0 0 0 0 0 1]

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential(name='model_for_handwritten_digits')
model.add(Input(shape=(784,)))
model.add(Dense(400, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(10, activation='softmax'))

# >>> model.summary()
# Model: "model_for_handwritten_digits"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 400)                 │         314,000 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 200)                 │          80,200 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_2 (Dense)                      │ (None, 10)                  │           2,010 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 396,210 (1.51 MB)
#  Trainable params: 396,210 (1.51 MB)
#  Non-trainable params: 0 (0.00 B)

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(learning_rate=0.001),
    metrics=[CategoricalAccuracy(name='accuracy')],
)
model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=15,
    validation_split=0.1,
    verbose=1,
)

