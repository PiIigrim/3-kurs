from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy

def DBSCAN(Data, eps, MinPts):
    labels = [0]*len(Data)  #устанавливаем все ID на 0
    Curr_ID = 0

    #выбор начальной точки для нового кластера
    for point in range(0, len(Data)):
        if not (labels[point] == 0):
           continue

        NeighborPoints = regionQuery(Data, point, eps)

        #если у точки меньше соседей чем MinPts, то это шум, иначе создаем кластер
        if len(NeighborPoints) < MinPts:
            labels[point] = -1
        else: 
           Curr_ID += 1
           growCluster(Data, labels, point, NeighborPoints, Curr_ID, eps, MinPts)

    return labels


def growCluster(Data, labels, point, NeighborPoints, Cluster_ID, eps, MinPts):
    #даем ID начальной точке
    labels[point] = Cluster_ID

    i = 0
    while i < len(NeighborPoints):
        new_point = NeighborPoints[i]

        if labels[new_point] == -1:
           labels[new_point] = Cluster_ID

        elif labels[new_point] == 0:
            labels[new_point] = Cluster_ID

            # находим всех соседей Pn
            PnNeighborPoints = regionQuery(Data, new_point, eps)

            #если точка имеет больше MinPts соседей, добавяем в массив поиска
            if len(PnNeighborPoints) >= MinPts:
                NeighborPoints = NeighborPoints + PnNeighborPoints
        i += 1


def regionQuery(Data, point, eps):
    neighbors = []
    for Pn in range(0, len(Data)):
        if numpy.linalg.norm(Data[point] - Data[Pn]) < eps:
           neighbors.append(Pn)
    return neighbors


centers = [[1, 0], [-2, -1], [0, -2]]
X, labels_true = make_blobs(n_samples=700, centers=centers, cluster_std=0.35, random_state=1)
X = StandardScaler().fit_transform(X)
labels =  DBSCAN(X, eps=0.35, MinPts=10)
plt.scatter(X[:, 0], X[:, 1], c = labels)
plt.show()
