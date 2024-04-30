#a * cos(bx) + c * sin(dx)

# вариант: 4

# а: 0.4

# b: 0.4

# c: 0.08

# d: 0.4

# входы:6

# НЭ в скрытом слое: 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

<<<<<<< HEAD
def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

def mse_gradient(actual, predicted):
    return (predicted - actual)

=======
>>>>>>> d1a31638d002002a1b0b5973e3a3329ae4e5323d
data = pd.read_csv('C:\\work\\2 semestr\\МРЗИС\\лаба3\\test.csv')
data = data.ffill()

#"ручной" проход
np.random.seed(0)

# input_weight = np.random.rand(1, 2)
# hidden_weight = np.random.rand(2, 2)
# output_weight = np.random.rand(2, 1)

# temp = data["y"].tail(3).to_numpy()

# #"для более простой обработки"
# x0 = temp[0].reshape(1, 1)
# x1 = temp[1].reshape(1, 1)
# x2 = temp[2].reshape(1, 1)

# xi_0 = x0 @ input_weight
# xh_0 = np.maximum(0, xi_0)
# xo_0 = xh_0 @ output_weight

# xi_1 = x1 @ input_weight
# xh = xh_0 @ hidden_weight
# xh_1 = np.maximum(0, xh + xi_1)
# xo_1 = xh_1 @ output_weight

# xi_2 = x2 @ input_weight
# xh = xh_1 @ hidden_weight
# xh_2 = np.maximum(0, xh + xi_2)
# xo_2 = xh_2 @ output_weight

#полный проход вперед
<<<<<<< HEAD
# i_weight = np.random.rand(1, 5) / 5 - .1
# h_weight = np.random.rand(5, 5) / 5 - .1
# h_bias = np.random.rand(1, 5) / 5 - .1

# o_weight = np.random.rand(5, 1) * 50
# o_bias = np.random.rand(1, 1)

# outputs = np.zeros(3)
# hiddens = np.zeros((3,5))
# prev_hidden = None
# sequence = data["y"].tail(3).to_numpy()

# #тоже что выше, но в лупе
# for i in range(3):
#     x = sequence[i].reshape(1, 1)

#     xi = x @ i_weight
#     if prev_hidden is None:
#         xh = xi
#     else:
#         xh = xi + prev_hidden @ h_weight + h_bias

#     xh = np.tanh(xh)
#     prev_hidden = xh
#     hiddens[i,] = xh

#     xo = xh @ o_weight + o_bias
#     outputs[i] = xo


# #backward
# actuals = data["y"].tail(3).to_numpy()
# loss_gradient = mse_gradient(actuals, outputs)

# next_hidden = None
# o_weight_grad, o_bias_grad, h_weight_grad, h_bias_grad, i_weight_grad = [0] * 5
# for i in range(2, -1, -1):
#     l_grad = loss_gradient[i].reshape(1, 1)

#     o_weight_grad += hiddens[i][:, np.newaxis] @ l_grad
#     o_bias_grad += np.mean(l_grad)

#     o_grad = l_grad @ o_weight.T

#     if next_hidden is None:
#         h_grad = o_grad
#     else:
#         h_grad = o_grad + next_hidden @ h_weight.T

#     tanh_deriv = 1 - hiddens[i, :][np.newaxis, :]
#     h_grad = np.multiply(h_grad, tanh_deriv)

#     next_hidden = h_grad

#     if i > 0:
#         h_weight_grad += hiddens[i - 1, :][:, np.newaxis] @ h_grad
#         h_bias_grad += np.mean(h_grad)
    
#     i_weight_grad += sequence[i].reshape(1, 1) @ h_grad

# lr = 1e-6

# i_weight -= i_weight_grad * lr
# h_weight -= h_weight_grad * lr
# h_bias -= h_bias_grad * lr
# o_weight -= o_weight_grad * lr
# o_bias -= o_bias_grad * lr
=======
i_weight = np.random.rand(1, 5) / 5 - .1
h_weight = np.random.rand(5, 5) / 5 - .1
h_bias = np.random.rand(1, 5) / 5 - .1

o_weight = np.random.rand(5, 1) * 50
o_bias = np.random.rand(1, 1)

outputs = np.zeros(3)
hiddens = np.zeros((3,5))
prev_hidden = None
sequence = data["y"].tail(3).to_numpy()

#тоже что выше, но в лупе
for i in range(3):
    x = sequence[i].reshape(1, 1)

    xi = x @ i_weight
    if prev_hidden is None:
        xh = xi
    else:
        xh = xi + prev_hidden @ h_weight + h_bias

    xh = np.tanh(xh)
    prev_hidden = xh
    hiddens[i,] = xh

    xo = xh @ o_weight + o_bias
    outputs[i] = xo


# x = data['x']
# y = data['y']

# plt.scatter(x, y)
# plt.show()
>>>>>>> d1a31638d002002a1b0b5973e3a3329ae4e5323d
