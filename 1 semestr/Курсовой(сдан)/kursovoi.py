from tkinter import *
from tkinter import ttk
import random
import mysql.connector as mysql

label_color = None
def change_background_color(color):
    global label_color
    label_color = color
    root.configure(bg=color)

color_options = ["Белый", "Темный", "Небесная синева", "Летняя трава", "Случайный"]

random_change = False
def change_color_option(option):
    global random_change
    if option == "Белый":
        random_change = False
        change_background_color("white")
    elif option == "Темный":
        random_change = False
        change_background_color("grey")
    elif option == "Небесная синева":
        random_change = False
        change_background_color("lightblue") 
    elif option == "Летняя трава":
        random_change = False
        change_background_color("lightgreen") 
    elif option == "Случайный":
        random_change = True
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        change_background_color(random_color)

def clear_frame(frame):
    info_text.destroy()
    for widget in frame.winfo_children():
        if not isinstance(widget, Menu):
            widget.destroy()

class Table:
    def __init__(self, chosen):
        self.chosen = chosen
        self.tv = None

    def show_table(self, table_positionX=10, table_positionY=10, clear=True, rows = None):
        global info_text
        if clear:
            clear_frame(root)

        if random_change == True:
            change_color_option("Случайный")

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')

        if rows == None:
            rows = cursor.fetchall()

        if self.tv:
            self.tv.destroy()

        frame = Frame(root)
        frame.place(x=table_positionX, y=table_positionY)
        cursor.reset()
        cursor.execute(f"SHOW COLUMNS FROM {self.chosen}")
        columns_names = [column[0] for column in cursor.fetchall()]

        scrollbar = Scrollbar(frame, orient="vertical")
        self.tv = ttk.Treeview(frame, columns = columns_names, show="headings", height="5", yscrollcommand=scrollbar.set, selectmode=BROWSE)
        self.tv.pack(side="left")
        scrollbar.config(command=self.tv.yview)
        scrollbar.pack(side="right", fill="y")

        for idx, column in enumerate(columns_names):
            self.tv.heading(idx, text=column)

        for i in rows:
            self.tv.insert('', 'end', values=i)

        con.commit()
        con.close()
        info_text = Label(root, text=f'Просмотр таблицы {self.chosen}', bg=label_color)
        info_text.place(x=10, y=150)

    def add_record(self):
        global info_text
        clear_frame(root)
        if random_change == True:
            change_color_option("Случайный")
        self.show_table(table_positionY=150, clear=False)
        info_text.destroy()

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')
        columns = [column[0] for column in cursor.description]
        con.close()

        entries = []
        labels = []
        for idx, column in enumerate(columns, start=1):
            label = Label(root, text=column, bg=label_color)
            label.place(x=10, y=10 + (idx - 1) * 20)
            labels.append(label)

            entry = Entry(root, width=30)
            entry.place(x=170, y=10 + (idx - 1) * 20)
            entries.append(entry)

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
        cursor = con.cursor()

        def handle_enter(event):
            values = [entry.get() for entry in entries]

            cursor.reset()
            cursor.execute(f'INSERT INTO {self.chosen} VALUES {tuple(values)};')
            con.commit()
            con.close()

            for entry in entries:
                entry.delete(0, END)

            self.show_table(table_positionY=150, clear=False)
            info_text.destroy()
            self.add_record()

        root.bind("<Return>", handle_enter)
        info_text = Label(root, text=f'Добавление данных в таблицу {self.chosen}', bg=label_color)
        info_text.place(x=10, y=290)

    def select(self):
        selected_items = self.tv.selection()[0]
        first_value = self.tv.item(selected_items)["values"][0]
        return first_value

    def delete_record(self):
        global info_text
        clear_frame(root)
        self.show_table()
        info_text.destroy()
        if random_change == True:
            change_color_option("Случайный")

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')
        first_column = cursor.column_names[0]

        def delete(event):
            first_value = self.select()
            cursor.reset()
            cursor.execute(f'DELETE FROM {self.chosen} WHERE {first_column} = "{first_value}"')
            con.commit()
            con.close()
            self.show_table()
            info_text.destroy()
            self.delete_record()

        root.bind("<Delete>", delete)

        info_text = Label(root, text=f'Удаление данных из таблицы {self.chosen}', bg=label_color)
        info_text.place(x=10, y=150)

    def sort_record(self, sorted = False, sorted_rows = None):
        global info_text
        clear_frame(root)
        if random_change == True:
            change_color_option("Случайный")
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
        cursor = con.cursor()
        if sorted == True:
            self.show_table(table_positionY=80, rows=sorted_rows)
            info_text.destroy()
        else:
            self.show_table(table_positionY=80)
            info_text.destroy()

        sort_options = ["Сортировать по возрастанию", "Сортировать по убыванию"]
        options_var = StringVar(value = sort_options[0])
        combobox_sort = ttk.Combobox(textvariable=options_var, values=sort_options, width=27)
        combobox_sort.place(x=10, y=10)

        cursor.execute(f"SHOW COLUMNS FROM {self.chosen}")
        columns_names = [column[0] for column in cursor.fetchall()]
        options_var = StringVar(value = columns_names[0])
        combobox_column = ttk.Combobox(textvariable=options_var, values=columns_names)
        combobox_column.place(x=200, y=10)
        def handle_sort(event):
            sort_type = combobox_sort.get()
            if sort_type == "Сортировать по возрастанию":
                sort_type = "asc"
            else:
                sort_type = "desc"

            column = combobox_column.get()
            con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM {self.chosen} ORDER BY {column} {sort_type}')
            sorted_rows = cursor.fetchall()
            self.show_table(table_positionY=80, rows=sorted_rows, clear=False)
            info_text.destroy()
            self.sort_record(sorted=True, sorted_rows=sorted_rows)

        root.bind("<Return>", handle_sort)

        info_text = Label(root, text=f'Сортировка данных в таблице {self.chosen}', bg=label_color)
        info_text.place(x=10, y=220)
    
root = Tk()
root.geometry("1500x600")
root.title("БД")
con = mysql.connect(host="localhost", user="root", password="1234567890", database="model_hub")
cursor = con.cursor()

table1 = Table("client")
table2 = Table("casting")
table3 = Table("model")
table4 = Table("agent")
table5 = Table("contract")

menubar = Menu(root)
root.config(menu=menubar)

show_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Показать", menu=show_menu)
show_menu.add_command(label=table1.chosen, command=table1.show_table)
show_menu.add_command(label=table2.chosen, command=table2.show_table)
show_menu.add_command(label=table3.chosen, command=table3.show_table)
show_menu.add_command(label=table4.chosen, command=table4.show_table)
show_menu.add_command(label=table5.chosen, command=table5.show_table)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Редактировать", menu=edit_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.add_record)
add_sub_menu.add_command(label=table2.chosen, command=table2.add_record)
add_sub_menu.add_command(label=table3.chosen, command=table3.add_record)
add_sub_menu.add_command(label=table4.chosen, command=table4.add_record)
add_sub_menu.add_command(label=table5.chosen, command=table5.add_record)

edit_menu.add_cascade(label="Добавить", menu=add_sub_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.delete_record)
add_sub_menu.add_command(label=table2.chosen, command=table2.delete_record)
add_sub_menu.add_command(label=table3.chosen, command=table3.delete_record)
add_sub_menu.add_command(label=table4.chosen, command=table4.delete_record)
add_sub_menu.add_command(label=table5.chosen, command=table5.delete_record)

edit_menu.add_cascade(label="Удалить", menu=add_sub_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.sort_record)
add_sub_menu.add_command(label=table2.chosen, command=table2.sort_record)
add_sub_menu.add_command(label=table3.chosen, command=table3.sort_record)
add_sub_menu.add_command(label=table4.chosen, command=table4.sort_record)
add_sub_menu.add_command(label=table5.chosen, command=table5.sort_record)

edit_menu.add_cascade(label="Сортировать", menu=add_sub_menu)

settings_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Настройки", menu=settings_menu)

color_submenu = Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label="Цвет", menu=color_submenu)

for color_option in color_options:
    color_submenu.add_command(label=color_option, command=lambda c=color_option: change_color_option(c))

info_text = Label(root, text="Выберите действие из меню", bg=label_color)
info_text.place(relx=0.4, rely=0.5)

def handle_exit(event):
    root.destroy()

root.bind("Q", handle_exit)

root.mainloop()