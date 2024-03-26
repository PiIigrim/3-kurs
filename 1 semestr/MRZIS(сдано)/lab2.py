import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

# генерация данных и запись в csv-файл, раскоментировать только для новых значений
dataX = np.random.normal(5, 0.8, 5000) 
dataX = dataX[dataX > 0]
dataY = np.random.normal(5, 0.8, 5000) 
dataY = dataY[dataY > 0]
with open('MRZIS\\NotRandomData.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ValueX', 'ValueY'])  # Добавляем заголовки для x и y
    for x, y in zip(dataX, dataY):
        csvwriter.writerow([x, y])

random_data = np.random.uniform(0.1, 10, 200)
data_with_random = np.concatenate((dataX, random_data), axis=None)
np.random.shuffle(data_with_random)

with open('MRZIS\\randomData.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ValueX', 'ValueY'])  # Добавляем заголовки для x и y
    for value in data_with_random:
        # Генерируем случайное значение для y
        y = np.random.normal(5, 0.8)
        csvwriter.writerow([value, y])
# генерация данных и запись в csv-файл, раскоментировать только для новых значений

not_random_data = pd.read_csv('MRZIS\\NotRandomData.csv')
data = pd.read_csv('MRZIS\\randomData.csv')
features = ["ValueX", "ValueY"]
data = data.dropna(subset=features)

#опредление кластеров
def random_centroids(data, k):
    centroids = []
    for _ in range(k):
        centroid = data.apply(lambda x: float(x.sample()))
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)

#нахождение растояния между значением и кластерами
def get_labels(data, centroids):
    distances = centroids.apply(lambda x: np.sqrt(((data - x)**2).sum(axis=1)))
    return distances.idxmin(axis=1)  #какое число к какому кластеру идет

#пересчет центроидов
def new_centroids(data, labels, k):
    return data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T

#рисование итераций(скорее всего не нужно)
# def plot_clusters(data, labels, centroids, iteration):
#     plt.figure(figsize=(8, 6))

#     for label in range(centroid_count):
#         cluster_data = data[labels == label]
#         plt.scatter(cluster_data['value'], [label] * len(cluster_data), label=f'Cluster {label}')

#     plt.scatter(centroids['value'], range(centroid_count), c='k', marker='x', s=100, label='Centroids')
#     plt.xlabel('Values')
#     plt.ylabel('Cluster')
#     plt.title(f'Iteration {iteration}')
#     plt.legend()
#     plt.grid(True)
#     plt.show()


#рисование графиков с начальными данными
# plt.figure(figsize=(8, 4))
# plt.subplot(1, 2, 1)
# plt.title("Без рандома")
# plt.scatter(range(len(not_random_data)), not_random_data, color='b', s=5)
# plt.xlabel("Индекс")
# plt.ylabel("Значения")

# plt.subplot(1, 2, 2)
# plt.title("С рандомом")
# plt.scatter(range(len(data)), data, color='b', s=5)
# plt.xlabel("Индекс")
# plt.ylabel("Значения")

# plt.tight_layout()
# plt.show()
#рисование графиков с данными

max_iteration = 100
iteration = 1
centroid_count = 3
anomaly_threshold = 1.8
centroids = random_centroids(data, centroid_count)
old_centroids = pd.DataFrame()

#изменение центроидов
while iteration < max_iteration and not centroids.equals(old_centroids):
    old_centroids = centroids
    labels = get_labels(data, centroids)
    centroids = new_centroids(data, labels, centroid_count)
    #plot_clusters(data, labels, centroids, iteration)
    iteration += 1

# distances = centroids.apply(lambda x: np.sqrt(((data - x)**2).sum(axis=1)))
# distances = distances.min(axis=1)
# threshold = np.percentile(distances, 96)
# #anomalies = data[distances>threshold]
# anomalies_indexes = np.where(distances > threshold)[0]
# anomalies = data.iloc[anomalies_indexes]
# colors = ['b', 'g', 'y']  # Задайте цвета для каждого кластера (в данном случае 3 цвета)

data['Label'] = labels  

#anomalies = data[abs(data['ValueX'] - data.groupby('Label')['ValueX'].transform('mean')) > std_threshold * data.groupby('Label')['ValueX'].transform('std')]
data['DistanceToCentroid'] = np.sqrt(((data[['ValueX', 'ValueY']] - centroids.loc[:, labels].values.T) ** 2).sum(axis=1))

# Определите аномалии на основе порогового значения
anomalies = data[data['DistanceToCentroid'] > anomaly_threshold]

colors = ['b', 'g', 'y']  


# Создайте график
plt.figure(figsize=(8, 4))
plt.title("Без класторизации")
plt.scatter(data['ValueX'], data['ValueY'], color='b', s=5)
plt.xlabel("Индекс")
plt.ylabel("Значения")

# plt.subplot(1, 2, 2)
# plt.title("С класторизацией")
# plt.scatter(data['ValueX'], data['ValueY'], color=[colors[i] for i in labels], s=5)
# plt.scatter(anomalies_indexes, anomalies, color='red', s=15)
# plt.xlabel("Индекс")
# plt.ylabel("Значения")
plt.figure(figsize=(8, 4))
plt.title("С кластеризацией и обнаружением аномалий")
plt.scatter(data['ValueX'], data['ValueY'], color=[colors[i] for i in labels], s=5)
plt.scatter(anomalies['ValueX'], anomalies['ValueY'], color='red', s=15, label='Аномалии')
plt.xlabel("ValueX")
plt.ylabel("ValueY")
plt.legend()
plt.show()