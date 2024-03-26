import tkinter as tk

# Функция для анимации
def inflate_oval():
    global top_y, bottom_y
    canvas.delete("oval")  # Удаляем предыдущий шарик
    top_y -= 1  # Увеличиваем координату верхней части шарика
    canvas.create_oval(center_x - radius, top_y, center_x + radius, bottom_y, fill="red", tags="oval")  # Создаем новый шарик
    if top_y > 10:
        root.after(100, inflate_oval)  # Повторяем анимацию через 100 миллисекунд

# Создаем основное окно
root = tk.Tk()
root.title("Продолговатый шарик")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

# Начальные параметры шарика
radius = 20  # Начальный радиус
center_x = canvas.winfo_reqwidth() / 2  # Координата x центра холста
top_y = canvas.winfo_reqheight() / 2  # Координата y верхней части шарика
bottom_y = (top_y + 2 * radius) + 50  # Координата y нижней части шарика

# Создаем продолговатый шарик
canvas.create_oval(center_x - radius, top_y, center_x + radius, bottom_y, fill="red", tags="oval")

# Запускаем анимацию
root.after(1000, inflate_oval)  # Запускаем через 1 секунду

root.mainloop()
