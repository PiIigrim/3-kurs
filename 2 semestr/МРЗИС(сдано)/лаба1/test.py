from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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

pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X_train_scaled)

# Объединяем преобразованные данные PCA с метками качества
pca_df = pd.DataFrame(data=X_train_pca, columns=['PC1', 'PC2'])
pca_df['Quality'] = y_train.values

# Группируем по меткам качества
quality_groups = pca_df.groupby('Quality')

# Рисуем график
plt.figure(figsize=(10, 6))

for name, group in quality_groups:
    plt.scatter(group['PC1'], group['PC2'], label=name)

plt.title('PCA Components with Wine Quality')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Quality')
plt.grid(True)
plt.show()

