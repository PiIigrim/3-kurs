import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data = []
data2 = []
y_output = []
#a * cos(bx) + c * sin(dx)
a = 0.4
b = 0.4
c = 0.08
d = 0.4

def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

def mse_gradient(actual, predicted):
    return (predicted - actual)

def create_real_data(number, aquracy = 0.1):
    x = 0
    while x < number:
        y = a * np.cos(b * x) + c * np.sin(d * x)
        data.append([x, y])
        x += aquracy
    stop_point = x
    return stop_point, data

def create_fakeReal_data(stop_point, number, aquracy = 0.1):
    x2 = stop_point
    while x2 < number + stop_point:
        y = a * np.cos(b * x2) + c * np.sin(d * x2)
        data2.append([x2, y])
        x2 += aquracy
    return data2

def init_params(layer_conf):
    layers = []
    for i in range(1, len(layer_conf)):
        k = 1/np.sqrt(layer_conf[i]["hidden"])
        i_weight = np.random.rand(layer_conf[i-1]["units"], layer_conf[i]["hidden"]) * 2 * k - k
        h_weight = np.random.rand(layer_conf[i]["hidden"], layer_conf[i]["hidden"]) * 2 * k - k
        h_bias = np.random.rand(1, layer_conf[i]["hidden"]) * 2 * k - k
        o_weight = np.random.rand(layer_conf[i]["hidden"], layer_conf[i]["output"]) * 2 * k - k
        o_bias = np.random.rand(1, layer_conf[i]["output"]) * 2 * k - k

        layers.append([i_weight, h_weight, h_bias, o_weight, o_bias])
    return layers

def forward(x, layers):
    hiddens, outputs = [], []
    for i in range(len(layers)):
        i_weight, h_weight, h_bias, o_weight, o_bias = layers[i]
        hidden = np.zeros((x.shape[0], i_weight.shape[1]))
        output = np.zeros((x.shape[0], o_weight.shape[1]))
        for j in range(x.shape[0]):
            input_x = x[j].reshape(1, -1) @ i_weight
            hidden_x = input_x + hidden[max(j-1, 0), :][np.newaxis, :] @ h_weight + h_bias
            hidden_x = np.tanh(hidden_x)
            hidden[j, :] = hidden_x

            output_x = hidden_x @ o_weight + o_bias
            output[j, :] = output_x
        hiddens.append(hidden)
        outputs.append(output)
    return hiddens, outputs[-1]

def backward(layers, x, lr, grad, hiddens):
    for i in range(len(layers)):
        i_weight, h_weight, h_bias, o_weight, o_bias = layers[i]
        hidden = hiddens[i]
        next_h_grad = None
        i_weight_grad, h_weight_grad, h_bias_grad, o_weight_grad, o_bias_grad = [0] * 5

        for j in range(x.shape[0] - 1, -1, -1):
            out_grad = grad[j, :][np.newaxis, :]

            o_weight_grad += hidden[j, :][:, np.newaxis] @ out_grad
            o_bias_grad += out_grad

            h_grad = out_grad.T @ o_weight.T

            if j < x.shape[0] - 1:
                hh_grad = next_h_grad @ h_weight.T
                h_grad += hh_grad

            tanh_deriv = 1 - hidden[j][np.newaxis, :] ** 2
            h_grad = np.multiply(h_grad, tanh_deriv)
            next_h_grad = h_grad.copy()

            if j > 0:
                h_weight_grad += hidden[j - 1].reshape(1, -1) @ h_grad
                h_bias_grad += h_grad

            #i_weight_grad += x[j, :][:, np.newaxis] @ h_grad
        
        lr = lr/x.shape[0]
        i_weight -= lr * i_weight_grad
        h_weight -= lr * h_weight_grad
        #h_bias -= lr * h_bias_grad
        #o_weight -= lr * o_weight_grad
        #o_bias -= lr * o_bias_grad
        layers[i] = [i_weight, h_weight, h_bias, o_weight, o_bias]
    return layers

epochs = 301
lr = 1e-6

stop_point, data = create_real_data(30, 0.07)
X = np.array([point[0] for point in data])
Y = np.array([point[1] for point in data])

data2 = create_fakeReal_data(stop_point, 100, 0.07)
X2 = np.array([point[0] for point in data2])
Y2 = np.array([point[1] for point in data2])

np.random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
layer_conf = [
    {"type": "input", "units": 1},
    {"type": "rnn", "hidden": 7, "output": 1},
]
layers = init_params(layer_conf)

for epoch in range(epochs):
    sequence_len = 7
    epoch_loss = 0
    for j in range(x_train.shape[0] - sequence_len):
        seq_x = x_train[j:(j+sequence_len)]
        seq_y = y_train[j:(j+sequence_len)]

        hiddens, outputs = forward(seq_x, layers)
        grad = mse_gradient(seq_y, outputs)
        params = backward(layers, seq_x, lr, grad, hiddens)
        epoch_loss += mse(seq_y, outputs)
    if epoch % 10 == 0:
        validation_loss = 0
        for j in range(x_test.shape[0] - sequence_len):
            seq_x = x_test[j:(j+sequence_len)]
            seq_y = y_test[j:(j+sequence_len)]

            _, outputs = forward(seq_x, layers)
            validation_loss += mse(seq_y, outputs)
        print(f"Epoch: {epoch}, loss: {epoch_loss/len(x_train)}, validation loss: {validation_loss/len(x_test)}")

#predict data with trained model
for j in range(len(X2) - sequence_len):
    seq_x = X2[j:(j+sequence_len)]
    _, outputs = forward(seq_x, layers)
    y_output.append(outputs[-1, 0])



plt.scatter(X, Y, s=5, color = 'blue')  #реальные данные
plt.scatter(X2, Y2, s=5, color = 'red', alpha=0.15)  #проверочные данные
X2 = X2[:-7]
X2.tolist()
plt.scatter(X2, y_output, s=5, color = 'green', alpha=0.5)  #прогноз
plt.show()
