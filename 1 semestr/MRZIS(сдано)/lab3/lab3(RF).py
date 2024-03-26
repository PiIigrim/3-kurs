import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

file = pd.read_csv('MRZIS\\lab3\\WineQT.csv')
#print(file['quality'].value_counts(normalize=True) * 100)
#print(file.describe())
#print(file.columns)
#модификация датасета
file = file[file['volatile acidity'] < 1]
file = file[file['sulphates'] < 1]
file = file[file['chlorides'] < 0.14]
file = file[file['free sulfur dioxide'] < 35]
file = file[(file['quality'] != 3) & (file['quality'] != 4) & (file['quality'] != 8)]
#print(file.describe())

col = ['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'total sulfur dioxide', 'pH','sulphates', 'alcohol']

X = pd.DataFrame()
for i in col:
    X[i] = file[i]
Y = file['quality']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

#вывод значимости признаков
# importances = model.feature_importances_
# indices = np.argsort(importances)[::-1]
# ar_f=[]
# for f, idx in enumerate(indices):
#     ar_f.append([round(importances[idx],4), col[idx]])
# print("Значимость признаков :", ar_f)
#вывод значимости признаков

#print("r2: ", r2_score(model.predict(X_test), y_test))
#print("Accuracy: ", metrics.accuracy_score(y_test, model.predict(X_test)))
#print(model.predict(X_test))
print(classification_report(y_test, model.predict(X_test)))
