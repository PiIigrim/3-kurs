import numpy as np
import pandas as pd

data = []
data2 = []
#a * cos(bx) + c * sin(dx)
a = 0.4
b = 0.4
c = 0.08
d = 0.4

x_values = np.arange(0, 10000, 1)

# Вычислите значения функции для каждого x
function_values = a * np.cos(b * x_values) + c * np.sin(d * x_values)

# Создайте DataFrame из значений функции
df = pd.DataFrame({'Wave': function_values})

# Сохраните DataFrame в файл CSV
csv_filename = 'function_values.csv'
df.to_csv(csv_filename, index=False)
