from dense import *
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical

def preprocess_data(x, y, limit):
    zero_index = np.where(y == 0)[0][:limit]
    one_index = np.where(y == 1)[0][:limit]
    all_indeces = np.hstack((zero_index, one_index))
    all_indeces = np.random.permutation(all_indeces)
    x, y = x[all_indeces], y[all_indeces]
    x = x.reshape(len(x), 1, 28, 28)
    x = x.astype('float32') / 255
    y = to_categorical(y)
    y = y.reshape(len(y), 2, 1)
    return x, y

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, y_train = preprocess_data(x_train, y_train, 100)
x_test, y_test = preprocess_data(x_test, y_test, 100)


network = [
    Convolutional((1, 28, 28), 3, 5),
    Sigmoid(),
    Reshape((5, 26, 26), (5 * 26 * 26, 1)),
    Dense(5 * 26 * 26, 100),
    Sigmoid(),
    Dense(100, 2),
    Sigmoid()
]

epochs = 20
learning_rate = 0.1

for e in range(epochs):
    error = 0
    for x, y in zip(x_train, y_train):
        output = x
        for layer in network:
            output = layer.forward(output)
        
        error += binary_cross_entropy(y, output)

        grad = binary_cross_entropy_prime(y, output)
        for layer in reversed(network):
            grad = layer.backward(grad, learning_rate)

    error /= len(x_train)
    print(f'{e + 1}/{epochs}, error={error}')

for x, y in zip(x_test, y_test):
    output = x
    for layer in network:
        output = layer.forward(output)
    if np.argmax(output) == np.argmax(y):
        print(f"CORRECT! Predicted: {np.argmax(output)}, true: {np.argmax(y)}")
    else:
        print(f"INCORRECT! Predicted: {np.argmax(output)}, true: {np.argmax(y)}")