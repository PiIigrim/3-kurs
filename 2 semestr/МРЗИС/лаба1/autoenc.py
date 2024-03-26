import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

file = pd.read_csv('C:\\work\\1 semestr\\MRZIS(сдано)\\lab3\\WineQT.csv')

file = file[file['volatile acidity'] < 1]
file = file[file['sulphates'] < 1]
file = file[file['chlorides'] < 0.14]
file = file[file['free sulfur dioxide'] < 35]
file = file[(file['quality'] != 3) & (file['quality'] != 4) & (file['quality'] != 8)]

X = file[['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'total sulfur dioxide', 'pH','sulphates', 'alcohol']]
Y = file['quality'].apply(lambda x: x - 5 if x >= 5 else x)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_tensor = torch.FloatTensor(X_train_scaled)
X_test_tensor = torch.FloatTensor(X_test_scaled)

class Autoencoder(nn.Module):
    def __init__(self, input_dim, encoding_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Linear(input_dim, encoding_dim)
        self.decoder = nn.Linear(encoding_dim, input_dim)

    def forward(self, x):
        encoded = torch.relu(self.encoder(x))
        decoded = torch.sigmoid(self.decoder(encoded))
        return decoded


input_dim = X_train_tensor.shape[1]
encoding_dim = 4

autoencoder = Autoencoder(input_dim, encoding_dim)

criterion = nn.MSELoss()
optimizer = optim.Adam(autoencoder.parameters(), lr=0.001)

# Обучение автоэнкодера
num_epochs = 2000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = autoencoder(X_train_tensor)
    loss = criterion(outputs, X_train_tensor)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Получение закодированных значений
encoded_X_train_tensor = autoencoder.encoder(X_train_tensor).detach().numpy()
encoded_X_test_tensor = autoencoder.encoder(X_test_tensor).detach().numpy()

# Обучение персептрона
mlp = MLPClassifier(hidden_layer_sizes=(5,), activation='logistic', max_iter=2000, learning_rate_init=0.12, alpha=3e-5)
mlp.fit(encoded_X_train_tensor, y_train)

predictions = mlp.predict(encoded_X_test_tensor)
print(classification_report(y_test, predictions))
accuracy = mlp.score(encoded_X_test_tensor, y_test)
print(f'Final accuracy: {accuracy:.3f}')

reconstructed_X_train_tensor = autoencoder.decoder(torch.FloatTensor(encoded_X_train_tensor)).detach().numpy()
reconstructed_X_test_tensor = autoencoder.decoder(torch.FloatTensor(encoded_X_test_tensor)).detach().numpy()

mse_test = mean_squared_error(X_test_tensor, reconstructed_X_test_tensor)
print("MSE на тестовом наборе данных:", mse_test)