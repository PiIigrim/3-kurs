from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import math

data = []
data2 = []
#a * cos(bx) + c * sin(dx)
a = 0.4
b = 0.4
c = 0.08
d = 0.4

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

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

def get_data(seq_len = 40):
    X2, Y2, X_val, Y_val = [], [], [], []

    num_records = len(X) - seq_len

    for i in range(num_records - seq_len):
        X2.append(X[i: i + seq_len])
        Y2.append(Y[i + seq_len])

    X2 = np.array(X2)
    X2 = np.expand_dims(X2, axis=2)
    Y2 = np.array(Y2)
    Y2 = np.expand_dims(Y2, axis=1)

    for i in range(num_records - seq_len, num_records):
        X_val.append(X[i: i + seq_len])
        Y_val.append(Y[i + seq_len])

    X_val = np.array(X_val)
    X_val = np.expand_dims(X_val, axis=2)
    Y_val = np.array(Y_val)
    Y_val = np.expand_dims(Y_val, axis=1)
    return X2, Y2, X_val, Y_val

stop_point, data = create_real_data(30, 0.1)
data2 = create_fakeReal_data(stop_point, 50, 0.5)

X = np.array([point[0] for point in data])
Y = np.array([point[1] for point in data])

data2X = np.array([point[0] for point in data2])
data2Y = np.array([point[1] for point in data2])

X2, Y2, X_val, Y_val = get_data(seq_len=100)

lr = 1e-3
num_epochs = 15
T = 100
hidden_dim = 2
output_dim = 1

bptt_truncate = 5
min_clip_value = -10
max_clip_value = 10
input_weight = np.random.uniform(0, 1, (hidden_dim, T))  #U
hidden_weight = np.random.uniform(0, 1, (hidden_dim, hidden_dim))  #W
output_weight = np.random.uniform(0, 1, (output_dim, hidden_dim))  #V

#и перед и зад, как говорится
for epoch in range(num_epochs):
    loss = 0.0

    for i in range(Y2.shape[0]):
        x, y = X2[i], Y2[i]
        prev_state = np.zeros((hidden_dim, 1))
        for t in range(T):
            new_input = np.zeros(x.shape)
            new_input[t] = x[t]
            mulinput = np.dot(input_weight, new_input)
            mulhidden = np.dot(hidden_weight, prev_state)
            add = mulinput + mulhidden
            state = sigmoid(add)
            muloutput = np.dot(output_weight, state)
            prev_state = state
        
        loss_per_record = (y - muloutput) ** 2 / 2
        loss += loss_per_record
    loss = loss / float(Y2.shape[0])

    val_loss = 0.0
    for i in range(Y_val.shape[0]):
        x, y = X_val[i], Y_val[i]
        prev_state = np.zeros((hidden_dim, 1))
        for t in range(T):
            new_input = np.zeros(x.shape)
            new_input[t] = x[t]
            mulinput = np.dot(input_weight, new_input)
            mulhidden = np.dot(hidden_weight, prev_state)
            add = mulinput + mulhidden
            state = sigmoid(add)
            muloutput = np.dot(output_weight, state)
            prev_state = state
        loss_per_record = (y - muloutput) ** 2 / 2
        val_loss += loss_per_record
    val_loss = val_loss / float(Y_val.shape[0])

    print(f"Epoch: {epoch + 1}, Loss: {loss}, Val Loss: {val_loss}")

    #train
    for i in range(Y2.shape[0]):
        x, y = X2[i], Y2[i]
        layers = []
        prev_state = np.zeros((hidden_dim, 1))

        dInput = np.zeros(input_weight.shape)
        dHidden = np.zeros(hidden_weight.shape)
        dOutput = np.zeros(output_weight.shape)

        dInput_t = np.zeros(input_weight.shape)
        dHidden_t = np.zeros(hidden_weight.shape)
        dOutput_t = np.zeros(output_weight.shape)

        dInput_i = np.zeros(input_weight.shape)
        dHidden_i = np.zeros(hidden_weight.shape)

        #forward
        for t in range(T):
            new_input = np.zeros(x.shape)
            new_input[t] = x[t]
            mulinput = np.dot(input_weight, new_input)
            mulhidden = np.dot(hidden_weight, prev_state)
            add = mulinput + mulhidden
            state = sigmoid(add)
            muloutput = np.dot(output_weight, state)
            layers.append({"state": state, "prev_state": prev_state})
            prev_state = state

        dMuloutput = (muloutput - y)

        #backward
        for t in range(T):
            dOutput_t = np.dot(dMuloutput, np.transpose(layers[t]["state"]))
            dsOutput = np.dot(np.transpose(output_weight), dMuloutput)

            ds = dsOutput
            dAdd = add * (1 - add) * ds

            dMulHidden = dAdd * np.ones_like(mulhidden)

            dPrev_state = np.dot(np.transpose(hidden_weight), dMulHidden)

            for i in range(t - 1, max(-1, t - bptt_truncate - 1), -1):
                ds = dsOutput + dPrev_state
                dAdd = add * (1 - add) * ds

                dMulHidden = dAdd * np.ones_like(mulhidden)
                dMulInput = dAdd * np.ones_like(mulinput)

                dHidden_i = np.dot(hidden_weight, layers[t]['prev_state'])
                dPrev_state = np.dot(np.transpose(hidden_weight), dMulHidden)

                new_input = np.zeros(x.shape)
                new_input[t] = x[t]
                dInput_i = np.dot(input_weight, new_input)
                dx = np.dot(np.transpose(input_weight), dMulInput)

                dInput_t += dInput_i
                dHidden_t += dHidden_i
            
            dOutput += dOutput_t
            dInput += dInput_t
            dHidden += dHidden_t

            if dInput.max() > max_clip_value:
                dInput[dInput > max_clip_value] = max_clip_value
            if dOutput.max() > max_clip_value:
                dOutput[dOutput > max_clip_value] = max_clip_value
            if dHidden.max() > max_clip_value:
                dHidden[dHidden > max_clip_value] = max_clip_value

            if dInput.min() < min_clip_value:
                dInput[dInput < min_clip_value] = min_clip_value
            if dOutput.min() < min_clip_value:
                dOutput[dOutput < min_clip_value] = min_clip_value
            if dHidden.min() < min_clip_value:
                dHidden[dHidden < min_clip_value] = min_clip_value
        #update
        input_weight -= lr * dInput
        hidden_weight -= lr * dHidden
        output_weight -= lr * dOutput

#predict
predicts = []
for i in range(data2Y.shape[0]):
    x, y = data2X[i], data2Y[i]
    prev_state = np.zeros((hidden_dim, 1))
    #forward
    for t in range(T):
        mulinput = np.dot(input_weight, x)
        mulhidden = np.dot(hidden_weight, prev_state)
        add = mulinput + mulhidden
        state = sigmoid(add)
        muloutput = np.dot(output_weight, state)
        prev_state = state

    predicts.append(muloutput)

predicts = np.array(predicts)

print(math.sqrt(mean_squared_error(data2Y, predicts[:, 0, 0])))

print(data2X)
print(data2Y)
print(predicts[:, 0, 0])

plt.scatter([point[0] for point in data], [point[1] for point in data], s=5, color = 'blue')  #реальные данные
plt.scatter([point[0] for point in data2], [point[1] for point in data2], s=5, color = 'red', alpha=0.15)  #реальные проверочные данные
plt.scatter(data2X, predicts[:, 0, 0], s=5, color = 'green')
plt.show()
