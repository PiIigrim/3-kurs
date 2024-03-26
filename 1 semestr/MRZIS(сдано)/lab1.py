import numpy as np
import matplotlib.pyplot as plt


def test(w, b):
    x = input("X: ")
    x_arrs = x.split()
    x_train = []
    for x_arr in x_arrs:
        values = x_arr.split(',')
        pair = [int(value) for value in values]
        x_train.append(pair)
    x_train = np.array(x_train)
    y = input("Y: ")
    y_train = []
    y_arrs = y.split()
    for y_arr in y_arrs:
        y_train.append(int(y_arr))
    y_train = np.array(y_train)

    line_x = np.array([w[0] - 10, w[1] + 10])
    line_y = (-w[0] * line_x - b) / w[1]

    y_train_min = min(y_train)
    y_train_max = max(y_train)
    x_1 = x_train[y_train == y_train_min]
    x_minus1 = x_train[y_train == y_train_max]

    plt.scatter(x_1[:, 0], x_1[:, 1], color='red', label='Class 1')
    plt.scatter(x_minus1[:, 0], x_minus1[:, 1], color='blue', label='Class -1')
    plt.plot(line_x, line_y, color='green', label='Decision Boundary')

    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_error_changes(errors_list):
    plt.plot(errors_list, marker='o', linestyle='-')
    plt.xlabel('Iteration')
    plt.ylabel('Errors')
    plt.title('Change in Errors over Iterations')
    plt.grid(True)
    plt.show()


x_train = np.array([[-4, -4], [-4, 2], [2, -4], [2, 2]])
y_train = np.array([1, 8, 1, 8])

n_train = len(x_train)
w = np.array([0.1, -0.1])
b = 0.1
N = 1000

learning_rate = 0.1
errors_list = []  # Список для отслеживания изменения числа ошибок на каждой итерации

for n in range(N):
    errors = 0
    for i in range(n_train):
        z = np.dot(w, x_train[i]) + b
        if z <= 0:
            y_pred = 1
        else:
            y_pred = 8

        if y_pred != y_train[i]:
            w = w + learning_rate * y_train[i] * x_train[i]
            b = b + learning_rate * y_train[i]
            errors += 1
    errors_list.append(errors)  # Добавляем число ошибок в список на каждой итерации

    if errors == 0:
        break

print("Final weights:", w)
print("Final bias:", b)

line_x = np.array([w[0] - 10, w[1] + 10])
line_y = (-w[0] * line_x - b) / w[1]

x_1 = x_train[y_train == 1]
x_minus1 = x_train[y_train == 8]

plt.scatter(x_1[:, 0], x_1[:, 1], color='red', label='Class 1')
plt.scatter(x_minus1[:, 0], x_minus1[:, 1], color='blue', label='Class -1')
plt.plot(line_x, line_y, color='green', label='Decision Boundary')

plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.ylabel("Y")
plt.xlabel("X")
plt.legend()
plt.grid(True)
plt.show()

#test(w, b)  # Вызываем функцию test с финальными весами и порогом
plot_error_changes(errors_list)  # Отображаем график изменения ошибок
