#5
import tkinter as tk
from tkinter import ttk

def select_rows():
    selected_rows = []
    if checkbutton_odd.get():
        selected_rows += [data[i] for i in range(len(data)) if i % 2 != 0]
    if checkbutton_even.get():
        selected_rows += [data[i] for i in range(len(data)) if i % 2 == 0]
    choice_var.set(selected_rows)

def clear_selection():
    checkbutton_odd.set(False)
    checkbutton_even.set(False)
    choice_var.set([])

def add_item():
    new_item = entry.get()
    if new_item:
        data.append(new_item)
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)

data = ["1", "2", "3", "4", "5", "6"]

app = tk.Tk()
app.title("Управление списком")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

checkbutton_odd = tk.BooleanVar()
checkbutton_even = tk.BooleanVar()

checkbutton_odd_checkbox = ttk.Checkbutton(frame, text="Выбрать нечетные строки", variable=checkbutton_odd)
checkbutton_odd_checkbox.grid(row=0, column=0, sticky="w")

checkbutton_even_checkbox = ttk.Checkbutton(frame, text="Выбрать четные строки", variable=checkbutton_even)
checkbutton_even_checkbox.grid(row=1, column=0, sticky="w")

select_button = ttk.Button(frame, text="Выбрать", command=select_rows)
select_button.grid(row=2, column=0, pady=10)

clear_button = ttk.Button(frame, text="Сбросить", command=clear_selection)
clear_button.grid(row=3, column=0)

choice_var = tk.StringVar()
choice_label = ttk.Label(frame, text="Выбранные строки:")
choice_label.grid(row=4, column=0, pady=10)

choice = ttk.Combobox(frame, textvariable=choice_var, state="readonly")
choice.grid(row=5, column=0, padx=10, pady=10)
choice.set("Выбранные строки")

add_frame = ttk.LabelFrame(frame, text="Добавить элемент")
add_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")

entry = ttk.Entry(add_frame)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = ttk.Button(add_frame, text="Добавить", command=add_item)
add_button.grid(row=1, column=0, padx=10, pady=10)

listbox = tk.Listbox(add_frame)
listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

for item in data:
    listbox.insert(tk.END, item)

app.mainloop()
