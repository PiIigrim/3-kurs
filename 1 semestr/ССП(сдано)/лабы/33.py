#8
import tkinter as tk
from tkinter import messagebox

def add_to_result():
    selected_items = listbox1.curselection()
    if selected_items:
        current_text = result_text.get("1.0", tk.END).strip()
        total_length = sum(len(listbox1.get(index)) for index in selected_items) + len(current_text)
        if total_length <= 100:
            for index in selected_items:
                result_text.insert(tk.END, listbox1.get(index) + "\n")
        else:
            messagebox.showinfo("Предупреждение", "Суммарное количество символов превышает 100 символов.")
    else:
        messagebox.showinfo("Предупреждение", "Выберите элемент из списка.")
        


def clear_result():
    result_text.delete("1.0", tk.END)

app = tk.Tk()
app.title("Множественный выбор элементов")

# Создаем список элементов
items = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5", "Элемент 6"]
listbox1 = tk.Listbox(app, selectmode=tk.MULTIPLE)
for item in items:
    listbox1.insert(tk.END, item)
listbox1.pack()

# Кнопки для добавления и очистки выбранных элементов
add_button = tk.Button(app, text="Добавить выбранные", command=add_to_result)
clear_button = tk.Button(app, text="Очистить результат", command=clear_result)
add_button.pack()
clear_button.pack()

# Соседний список выбранных элементов
result_text = tk.Text(app, height=5, width=30)
result_text.pack()

app.mainloop()
