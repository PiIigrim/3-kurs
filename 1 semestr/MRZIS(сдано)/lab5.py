import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Layer_Dense:
    def __init__(self, num_inputs, num_neurons):
        self.weight = 0.01 * np.random.randn(num_inputs, num_neurons)
        self.biases = np.zeros((1, num_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weight) + self.biases

    def backward(self, dvalues):
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs = np.dot(dvalues, self.weight.T)

class Softmax:
    def forward(self, inputs):
        self.inputs = inputs
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

    def backward(self, dvalues):
        self.dinputs = np.empty_like(dvalues)
        for index, (single_out, single_dvalues) in enumerate(zip(self.output, dvalues)):
            single_out = single_out.reshape(-1, 1)
            jacobian_matrix = np.diagflat(single_out) - np.dot(single_out, single_out.T)
            self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)

class Optimazer_Adam():
    def __init__(self, learning_rate=0.001, decay = 0., epsilon = 1e-7, beta_1 = 0.9, beta_2 = 0.999):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon
        self.beta_1 = beta_1
        self.beta_2 = beta_2

    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate =self.learning_rate * (1. / (1. + self.decay * self.iterations))
    
    def update_params(self, layer):
        if not hasattr(layer, 'weight_cache'):
            layer.weight_momentums = np.zeros_like(layer.weight)
            layer.weight_cache = np.zeros_like(layer.weight)
            layer.bias_momentums = np.zeros_like(layer.biases)
            layer.bias_cache = np.zeros_like(layer.biases)

        layer.weight_momentums = self.beta_1 * layer.weight_momentums + (1 - self.beta_1) * layer.dweights
        layer.bias_momentums = self.beta_1 * layer.bias_momentums + (1 - self.beta_1) * layer.dbiases

        weight_momentums_corrected = layer.weight_momentums / (1 - self.beta_1 ** (self.iterations + 1))
        bias_momentums_corrected = layer.bias_momentums / (1 - self.beta_1 ** (self.iterations + 1))
        layer.weight_cache = self.beta_2 * layer.weight_cache + (1 - self.beta_2) * layer.dweights ** 2
        layer.bias_cache = self.beta_2 * layer.bias_cache + (1 - self.beta_2) * layer.dbiases ** 2

        weight_cache_corrected = layer.weight_cache / (1 - self.beta_2 ** (self.iterations + 1))
        bias_cache_corrected = layer.bias_cache / (1 - self.beta_2 ** (self.iterations + 1))

        layer.weight += -self.current_learning_rate * weight_momentums_corrected / (np.sqrt(weight_cache_corrected) + self.epsilon)
        layer.biases += -self.current_learning_rate * bias_momentums_corrected / (np.sqrt(bias_cache_corrected) + self.epsilon)

    def post_update_params(self):
        self.iterations += 1

class Loss:
    def calc(self, output, y):
        sample_losses = self.forward(output, y)
        return np.mean(sample_losses)

class Loss_CCE(Loss):
    def forward(self, y_pred, y_real):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        if len(y_real.shape) == 1:
            correct_conf = y_pred_clipped[range(samples), y_real]
        elif len(y_real.shape) == 2:
            correct_conf = np.sum(y_pred_clipped*y_real, axis=1)
        neg_log_likehoods = -np.log(correct_conf)
        return neg_log_likehoods

    def backward(self, dvalues, y_real):
        samples = len(dvalues)
        labels = len(dvalues[0])
        if len(y_real.shape) == 1:
            y_real = np.eye(labels)[y_real]
        self.dinputs = -y_real / dvalues
        self.dinputs = self.dinputs / samples

class Loss_CCE_and_Softmax:
    def __init__(self):
        self.activation = Softmax()
        self.loss = Loss_CCE()
    
    def forward(self, inputs, y_true):
        self.activation.forward(inputs)
        self.output = self.activation.output
        return self.loss.calc(self.output, y_true)

    def backward(self, dvalues, y_true):
        samples = len(dvalues)
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)
        self.dinputs = dvalues.copy()
        self.dinputs[range(samples), y_true] -= 1
        self.dinputs = self.dinputs / samples


file = pd.read_csv('1 semestr\\MRZIS\\lab3\\WineQT.csv')
#модификация датасета
file = file[file['volatile acidity'] < 1]
file = file[file['sulphates'] < 1]
file = file[file['chlorides'] < 0.14]
file = file[file['free sulfur dioxide'] < 35]
file = file[(file['quality'] != 3) & (file['quality'] != 4) & (file['quality'] != 8)]

col = ['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'total sulfur dioxide', 'pH','sulphates', 'alcohol']

X = pd.DataFrame()
for i in col:
    X[i] = file[i]

Y = file['quality'].apply(lambda x: x - 5 if x>=5 else x)

X_train, X_test, y_train, y_test = train_test_split(X, X, test_size=0.2)

activation = Softmax()
autoencoder_input_layer = Layer_Dense(len(col), 4)
autoencoder_hidden_layer = Layer_Dense(4, 4)
autoencoder_output_layer = Layer_Dense(4, 8)
loss_func = Loss_CCE_and_Softmax()
optimazer = Optimazer_Adam(learning_rate=0.12, decay=3e-5)

print("Обчение автоенкодера")
for epoch in range(500):
    autoencoder_input_layer.forward(X_train)
    activation.forward(autoencoder_input_layer.output)

    autoencoder_hidden_layer.forward(activation.output)
    activation.forward(autoencoder_hidden_layer.output)

    autoencoder_output_layer.forward(activation.output)

    loss = loss_func.forward(autoencoder_output_layer.output, y_train)

    predictions = np.argmax(loss_func.output, axis=1)
    if len(y_train.shape) == 2:
        y_train = np.argmax(y_train, axis=1)
    accuracy = np.mean(predictions==y_train)
    if not epoch % 100:
        print(f'epoch: {epoch}, ' + f'acc: {accuracy:.3f}, ' + f'loss: {loss:.3f}, ' + f'lr: {optimazer.current_learning_rate}')
    
    loss_func.backward(loss_func.output, y_train)
    autoencoder_output_layer.backward(loss_func.dinputs)

    activation.backward(autoencoder_output_layer.dinputs)
    autoencoder_hidden_layer.backward(activation.dinputs)

    activation.backward(autoencoder_hidden_layer.dinputs)
    autoencoder_input_layer.backward(activation.dinputs)

    optimazer.pre_update_params()
    optimazer.update_params(autoencoder_input_layer)
    optimazer.update_params(autoencoder_hidden_layer)
    optimazer.update_params(autoencoder_output_layer)
    optimazer.post_update_params()

autoencoder_input_layer.forward(X)
activation.forward(autoencoder_input_layer.output)
autoencoder_hidden_layer.forward(activation.output)
# print("hidden: ", autoencoder_hidden_layer.output)
activation.forward(autoencoder_hidden_layer.output)
# print("after activation: ", activation.output)
autoencoder_output_layer.forward(activation.output)
# print("output: ", autoencoder_output_layer.output)
X_enc = autoencoder_output_layer.output

input_layer = Layer_Dense(len(col), 8)
hidden_layer = Layer_Dense(8, 8)
output_layer = Layer_Dense(8, 3)
X_train, X_test, y_train, y_test = train_test_split(X_enc, Y, test_size=0.2)
print("обучение перептрона на данных с автоенкодра")
for epoch in range(500):
    input_layer.forward(X_train)
    activation.forward(input_layer.output)

    hidden_layer.forward(activation.output)
    activation.forward(hidden_layer.output)

    output_layer.forward(activation.output)

    loss = loss_func.forward(output_layer.output, y_train)

    predictions = np.argmax(loss_func.output, axis=1)
    if len(y_train.shape) == 2:
        y_train = np.argmax(y_train, axis=1)
    accuracy = np.mean(predictions==y_train)
    if not epoch % 100:
        print(f'epoch: {epoch}, ' + f'acc: {accuracy:.3f}, ' + f'loss: {loss:.3f}, ' + f'lr: {optimazer.current_learning_rate}')
    
    loss_func.backward(loss_func.output, y_train)
    output_layer.backward(loss_func.dinputs)

    activation.backward(output_layer.dinputs)
    hidden_layer.backward(activation.dinputs)

    activation.backward(hidden_layer.dinputs)
    input_layer.backward(activation.dinputs)

    optimazer.pre_update_params()
    optimazer.update_params(input_layer)
    optimazer.update_params(hidden_layer)
    optimazer.update_params(output_layer)
    optimazer.post_update_params()

input_layer.forward(X_test)
activation.forward(input_layer.output)

hidden_layer.forward(activation.output)
activation.forward(hidden_layer.output)
output_layer.forward(activation.output)

loss = loss_func.forward(output_layer.output, y_test)

predictions = np.argmax(loss_func.output, axis=1)

if len(y_test.shape) == 2:
    y_test = np.argmax(y_test, axis=1)

accuracy = np.mean(predictions==y_test)
print(f'final acc: {accuracy:.3f}, ' + f'loss: {loss:.3f}')