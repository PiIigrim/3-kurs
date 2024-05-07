from tkinter import *
from tkinter import ttk, filedialog
import random, csv
import mysql.connector as mysql
import re

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

def read_vcf(vcf_file):
    with open(vcf_file, "r") as file:
        vcf_content = file.read()

    name = re.search(r'FN:(.*)', vcf_content).group(1)
    phone = re.search(r'TEL;TYPE=CELL:(.*)', vcf_content).group(1)
    email = re.search(r'EMAIL;TYPE=INTERNET:(.*)', vcf_content).group(1)
    bday = re.search(r'BDAY:(.*)', vcf_content).group(1)

    return name, phone, email, bday

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

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
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
        self.show_table(table_positionY=110, clear=False)
        info_text.destroy()

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
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

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
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
        info_text.place(x=10, y=240)

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

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')
        first_column = cursor.column_names[0]

        def delete(event):
            first_value = self.select()
            cursor.reset()
            cursor.execute(f'DELETE FROM {self.chosen} WHERE {first_column} = {first_value}')
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
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
        cursor = con.cursor()
        if sorted == True:
            self.show_table(table_positionY=50, rows=sorted_rows)
            info_text.destroy()
        else:
            self.show_table(table_positionY=50)
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
            con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM {self.chosen} ORDER BY {column} {sort_type}')
            sorted_rows = cursor.fetchall()
            self.show_table(table_positionY=80, rows=sorted_rows, clear=False)
            info_text.destroy()
            self.sort_record(sorted=True, sorted_rows=sorted_rows)

        root.bind("<Return>", handle_sort)

        info_text = Label(root, text=f'Сортировка данных в таблице {self.chosen}', bg=label_color)
        info_text.place(x=10, y=180)
    def save_to_csv(self):
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')
        rows = cursor.fetchall()
        con.close()
        
        filename = f"{self.chosen}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(rows)

    def vcf_export(self):
        global info_text
        clear_frame(root)
        self.show_table()
        info_text.destroy()
        if random_change == True:
            change_color_option("Случайный")

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {self.chosen}')

        def export(event):
            selected_items = self.tv.selection()
            values = self.tv.item(selected_items)["values"]
            phone, full_name, email, bday = values[0], values[1], values[2], values[3]
            try:
                second_name = full_name.split()[1]
            except:
                second_name = ""
            first_name = full_name.split()[0]
            bday = bday.replace("-", "")
            vcf_content = f"""BEGIN:VCARD
VERSION:4.0
N:{second_name};{first_name}
FN:{full_name}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=INTERNET:{email}
BDAY:{bday}
END:VCARD
"""
            with open(f"{first_name}.vcf", "w") as vcf_file:
                vcf_file.write(vcf_content)

        root.bind("<Return>", export)

        info_text = Label(root, text=f'Экспорт данных из таблицы {self.chosen} в формат VCF', bg=label_color)
        info_text.place(x=10, y=150)

    def vcf_import(self):
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
        cursor = con.cursor()
        file_path = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
        if file_path:
            name, phone, email, bday = read_vcf(file_path)
            values = [phone, name, email, bday]
            cursor.reset()
            cursor.execute(f'INSERT INTO {self.chosen} VALUES {tuple(values)};')
            con.commit()
            con.close()
            self.show_table()

    
root = Tk()
root.geometry("850x300")
root.resizable(False, False)
root.title("БД")
con = mysql.connect(host="localhost", user="root", password="1234567890", database="giis2")
cursor = con.cursor()

table1 = Table("contacts")

menubar = Menu(root)
root.config(menu=menubar)

show_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Показать", menu=show_menu, command=table1.show_table)
show_menu.add_command(label=table1.chosen, command=table1.show_table)


edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Редактировать", menu=edit_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.add_record)

edit_menu.add_cascade(label="Добавить", menu=add_sub_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.delete_record)

edit_menu.add_cascade(label="Удалить", menu=add_sub_menu)

add_sub_menu = Menu(edit_menu, tearoff=0)
add_sub_menu.add_command(label=table1.chosen, command=table1.sort_record)

edit_menu.add_cascade(label="Сортировать", menu=add_sub_menu)

settings_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Настройки", menu=settings_menu)

color_submenu = Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label="Цвет", menu=color_submenu)

for color_option in color_options:
    color_submenu.add_command(label=color_option, command=lambda c=color_option: change_color_option(c))

save_submenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Сохранить в CSV", command=table1.save_to_csv)

vcf_submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="VCF", menu=vcf_submenu)

vcf_submenu.add_command(label="Экспорт в VCF", command=table1.vcf_export)
vcf_submenu.add_command(label="Импорт из VCF", command=table1.vcf_import)

info_text = Label(root, text="Выберите действие из меню", bg=label_color)
info_text.place(relx=0.4, rely=0.5)

def handle_exit(event):
    root.destroy()

root.bind("Q", handle_exit)

root.mainloop()