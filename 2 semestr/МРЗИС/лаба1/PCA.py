import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# file = pd.read_csv('C:\\work\\1 semestr\\MRZIS(сдано)\\lab3\\WineQT.csv')

# file = file[file['volatile acidity'] < 1]
# file = file[file['sulphates'] < 1]
# file = file[file['chlorides'] < 0.14]
# file = file[file['free sulfur dioxide'] < 35]
# file = file[(file['quality'] != 3) & (file['quality'] != 4) & (file['quality'] != 8)]

# X = file[['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'total sulfur dioxide', 'pH','sulphates', 'alcohol']]
# Y = file['quality'].apply(lambda x: x - 5 if x >= 5 else x)

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
X_train_scaled = np.array([[-2, 2], [2, -2]])
X_mean = X_train_scaled.mean()
X_centered = X_train_scaled - X_mean
cov = np.cov(X_train_scaled.T)

eigenvalues, eigenvectors = np.linalg.eig(cov)

first_eigenvector = list(reversed(eigenvectors[0]))
second_eigenvector = list(reversed(eigenvectors[1]))

first_PC = X_centered * first_eigenvector
second_PC = X_centered * second_eigenvector

first_PC = first_PC.sum(axis=1)
second_PC = second_PC.sum(axis=1)

reconstructed_X_train_scaled = np.dot(np.array([first_PC, second_PC]).T, eigenvectors[:2, :]) + X_mean


mse = mean_squared_error(X_train_scaled, reconstructed_X_train_scaled)
print("MSE между исходными и восстановленными данными:", mse)
