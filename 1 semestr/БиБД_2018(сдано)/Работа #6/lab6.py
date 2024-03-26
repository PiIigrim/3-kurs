from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tabulate

entries = []
labels = []

def deleteWidgets():
    for entry in entries:
        if entry:
            entry.destroy()
    for label in labels:
        if label:
            label.destroy()

def table1():
    global f_number, f_adress, f_FIO, chosen, combo_out
    chosen = "table1"
    deleteWidgets()
    f_number = Entry(root, width=30)
    f_number.place(x=170, y=50)
    f_adress = Entry(root, width=30)
    f_adress.place(x=170, y=70)
    f_FIO = Entry(root, width=30)
    f_FIO.place(x=170, y=90)

    f_number_label = Label(root, text="Номер")
    f_number_label.place(x=10, y=50)
    f_adress_label = Label(root, text="Адресс")
    f_adress_label.place(x=10, y=70)
    f_FIO_label = Label(root, text="ФИО")
    f_FIO_label.place(x=10, y=90)

    entries.append(f_number)
    entries.append(f_adress)
    entries.append(f_FIO)
    labels.append(f_number_label)
    labels.append(f_adress_label)
    labels.append(f_FIO_label)

    text_label2 = Label(root, text=chosen)
    text_label2.place(x=85, y=115)
    text_label3 = Label(root, text=chosen)
    text_label3.place(x=110, y=190)

    def on_combobox_change(event):
        global combo_out
        combo_out = combobox.get()

    options = ["№", "adress", "FIO"]
    options_var = StringVar(value=options[0])
    combobox = ttk.Combobox(textvariable=options_var, values=options)
    combobox.place(x=150, y=115)
    combobox.bind("<<ComboboxSelected>>", on_combobox_change)

    def on_combobox_change2(event):
        global combo_out_what
        combo_out_what = combobox_edit1.get()

    options_var1 = StringVar(value=options[0])
    combobox_edit1 = ttk.Combobox(textvariable=options_var1, values=options)
    combobox_edit1.place(x=80, y=150)
    combobox_edit1.bind("<<ComboboxSelected>>", on_combobox_change2)

    def on_combobox_change3(event):
        global combo_out_where
        combo_out_where = combobox_edit2.get()

    options_var2 = StringVar(value=options[0])
    combobox_edit2 = ttk.Combobox(textvariable=options_var2, values=options)
    combobox_edit2.place(x=400, y=150)
    combobox_edit2.bind("<<ComboboxSelected>>", on_combobox_change3)

    def on_combobox_change4(event):
        global combo_out2
        combo_out2 = combobox_select.get()

    options_var3 = StringVar(value=options[0])
    combobox_select = ttk.Combobox(textvariable=options_var3, values=options)
    combobox_select.place(x=180, y=190)
    combobox_select.bind("<<ComboboxSelected>>", on_combobox_change4)

    def on_combobox_change5(event):
        global combo_out3
        combo_out3 = combobox_sort.get()

    options_var4 = StringVar(value=options[0])
    combobox_sort = ttk.Combobox(textvariable=options_var4, values=options)
    combobox_sort.place(x=240, y=230)
    combobox_sort.bind("<<ComboboxSelected>>", on_combobox_change5)

    show(chosen)

def table2():
    global f_category, f_min_age, f_max_age, chosen, combo_out
    chosen = "table2"
    deleteWidgets()
    f_category = Entry(root, width=30)
    f_category.place(x=170, y=50)
    f_min_age = Entry(root, width=30)
    f_min_age.place(x=170, y=70)
    f_max_age = Entry(root, width=30)
    f_max_age.place(x=170, y=90)

    f_category_label = Label(root, text="Категория")
    f_category_label.place(x=10, y=50)
    f_min_age_label = Label(root, text="Минимальный возраст")
    f_min_age_label.place(x=10, y=70)
    f_max_age_label = Label(root, text="Максимальный возраст")
    f_max_age_label.place(x=10, y=90)

    entries.append(f_category)
    entries.append(f_min_age)
    entries.append(f_max_age)
    labels.append(f_category_label)
    labels.append(f_min_age_label)
    labels.append(f_max_age_label)

    text_label2 = Label(root, text=chosen)
    text_label2.place(x=85, y=115)
    text_label3 = Label(root, text=chosen)
    text_label3.place(x=110, y=190)

    def on_combobox_change(event):
        global combo_out
        combo_out = combobox.get()

    options = ["category", "min_age", "max_age"]
    options_var = StringVar(value=options[0])
    combobox = ttk.Combobox(textvariable=options_var, values=options)
    combobox.place(x=150, y=115)
    combobox.bind("<<ComboboxSelected>>", on_combobox_change)

    def on_combobox_change2(event):
        global combo_out_what
        combo_out_what = combobox_edit1.get()

    options_var1 = StringVar(value=options[0])
    combobox_edit1 = ttk.Combobox(textvariable=options_var1, values=options)
    combobox_edit1.place(x=80, y=150)
    combobox_edit1.bind("<<ComboboxSelected>>", on_combobox_change2)

    def on_combobox_change3(event):
        global combo_out_where
        combo_out_where = combobox_edit2.get()

    options_var2 = StringVar(value=options[0])
    combobox_edit2 = ttk.Combobox(textvariable=options_var2, values=options)
    combobox_edit2.place(x=400, y=150)
    combobox_edit2.bind("<<ComboboxSelected>>", on_combobox_change3)

    def on_combobox_change4(event):
        global combo_out2
        combo_out2 = combobox_select.get()

    options_var3 = StringVar(value=options[0])
    combobox_select = ttk.Combobox(textvariable=options_var3, values=options)
    combobox_select.place(x=180, y=190)
    combobox_select.bind("<<ComboboxSelected>>", on_combobox_change4)

    def on_combobox_change5(event):
        global combo_out3
        combo_out3 = combobox_sort.get()

    options_var4 = StringVar(value=options[0])
    combobox_sort = ttk.Combobox(textvariable=options_var4, values=options)
    combobox_sort.place(x=240, y=230)
    combobox_sort.bind("<<ComboboxSelected>>", on_combobox_change5)

    show(chosen)

def table3():
    global f_number, f_category, f_teacher, chosen, combo_out
    chosen = "table3"
    deleteWidgets()
    f_number = Entry(root, width=30)
    f_number.place(x=170, y=50)
    f_category = Entry(root, width=30)
    f_category.place(x=170, y=70)
    f_teacher = Entry(root, width=30)
    f_teacher.place(x=170, y=90)

    f_number_label = Label(root, text="Номер")
    f_number_label.place(x=10, y=50)
    f_category_label = Label(root, text="Категория")
    f_category_label.place(x=10, y=70)
    f_teacher_label = Label(root, text="Учитель")
    f_teacher_label.place(x=10, y=90)

    entries.append(f_number)
    entries.append(f_category)
    entries.append(f_teacher)
    labels.append(f_number_label)
    labels.append(f_category_label)
    labels.append(f_teacher_label)

    text_label2 = Label(root, text=chosen)
    text_label2.place(x=85, y=115)
    text_label3 = Label(root, text=chosen)
    text_label3.place(x=110, y=190)

    def on_combobox_change(event):
        global combo_out
        combo_out = combobox.get()

    options = ["№", "category", "teacher"]
    options_var = StringVar(value=options[0])
    combobox = ttk.Combobox(textvariable=options_var, values=options)
    combobox.place(x=150, y=115)
    combobox.bind("<<ComboboxSelected>>", on_combobox_change)

    def on_combobox_change2(event):
        global combo_out_what
        combo_out_what = combobox_edit1.get()

    options_var1 = StringVar(value=options[0])
    combobox_edit1 = ttk.Combobox(textvariable=options_var1, values=options)
    combobox_edit1.place(x=80, y=150)
    combobox_edit1.bind("<<ComboboxSelected>>", on_combobox_change2)

    def on_combobox_change3(event):
        global combo_out_where
        combo_out_where = combobox_edit2.get()

    options_var2 = StringVar(value=options[0])
    combobox_edit2 = ttk.Combobox(textvariable=options_var2, values=options)
    combobox_edit2.place(x=400, y=150)
    combobox_edit2.bind("<<ComboboxSelected>>", on_combobox_change3)

    def on_combobox_change4(event):
        global combo_out2
        combo_out2 = combobox_select.get()

    options_var3 = StringVar(value=options[0])
    combobox_select = ttk.Combobox(textvariable=options_var3, values=options)
    combobox_select.place(x=180, y=190)
    combobox_select.bind("<<ComboboxSelected>>", on_combobox_change4)

    def on_combobox_change5(event):
        global combo_out3
        combo_out3 = combobox_sort.get()

    options_var4 = StringVar(value=options[0])
    combobox_sort = ttk.Combobox(textvariable=options_var4, values=options)
    combobox_sort.place(x=240, y=230)
    combobox_sort.bind("<<ComboboxSelected>>", on_combobox_change5)
    
    show(chosen)

def add_record():
    global local_state, local_state_rows
    local_state = "no"
    local_state_rows = "no"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()

    match chosen:
        case "table1":
            cursor.execute(f'INSERT INTO table1 VALUES {f_number.get(), f_adress.get(), f_FIO.get()};')
            
            con.commit()
            con.close()

            f_number.delete(0, END)
            f_adress.delete(0, END)
            f_FIO.delete(0, END)
        case "table2":
            cursor.execute(f'INSERT INTO table2 VALUES {f_category.get(), f_min_age.get(), f_max_age.get()};')
            
            con.commit()
            con.close()

            f_category.delete(0, END)
            f_min_age.delete(0, END)
            f_max_age.delete(0, END)
        case "table3":
            cursor.execute(f'INSERT INTO table3 VALUES {f_number.get(), f_category.get(), f_teacher.get()};')
            
            con.commit()
            con.close()

            f_number.delete(0, END)
            f_category.delete(0, END)
            f_teacher.delete(0, END)

    show(chosen)

def show(chosen):
    global local_state, local_state_rows
    local_state = "no"
    local_state_rows = "no"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {chosen}')
    rows = cursor.fetchall()
    frame = Frame(root)
    frame.place(x=10, y=300)
    tv = ttk.Treeview(frame, columns=(1, 2, 3), show="headings", height="5")
    tv.pack()
    match chosen:
        case "table1":
            tv.heading(1, text="№")
            tv.heading(2, text="adress")
            tv.heading(3, text="FIO")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table2":
            tv.heading(1, text="Category")
            tv.heading(2, text="Minimum аge")
            tv.heading(3, text="Maximum аge")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table3":
            tv.heading(1, text="№")
            tv.heading(2, text="Category")
            tv.heading(3, text="Teacher")

            for i in rows:
                tv.insert('', 'end', values=i)

    con.commit()
    con.close()

def delete_record():
    global local_state, local_state_rows
    local_state = "no"
    local_state_rows = "no"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()

    cursor.execute(f'DELETE FROM {chosen} WHERE {combo_out} = "{del_entry.get()}"')

    con.commit()
    con.close()
    show(chosen)

def update_record():
    global local_state, local_state_rows
    local_state_rows = "no"
    local_state = "no"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(f'UPDATE {chosen} SET {combo_out_what} = "{upd_entry2.get()}" WHERE {combo_out_where} = "{upd_entry1.get()}"')
    con.commit()
    con.close()
    show(chosen)

def select_record():
    global local_state, local_state_rows
    local_state = "search"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {chosen} WHERE {combo_out2} = "{sel_entry.get()}"')
    rows = cursor.fetchall()
    local_state_rows = rows
    frame = Frame(root)
    frame.place(x=10, y=300)
    tv = ttk.Treeview(frame, columns=(1, 2, 3), show="headings", height="5")
    tv.pack()
    match chosen:
        case "table1":
            tv.heading(1, text="№")
            tv.heading(2, text="adress")
            tv.heading(3, text="FIO")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table2":
            tv.heading(1, text="Category")
            tv.heading(2, text="Minimum аge")
            tv.heading(3, text="Maximum аge")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table3":
            tv.heading(1, text="№")
            tv.heading(2, text="Category")
            tv.heading(3, text="Teacher")

            for i in rows:
                tv.insert('', 'end', values=i)
    con.commit()
    con.close()

def sort_record():
    global local_state, local_state_rows, local_state_sort
    local_state = "sort"
    if sort_entry.get() == "убыв":
        sort = "desc"
        local_state_sort = "desc"
    else:
        sort = "asc"
        local_state_sort = "asc"
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {chosen} ORDER BY {combo_out3} {sort}')
    rows = cursor.fetchall()
    local_state_rows = rows
    frame = Frame(root)
    frame.place(x=10, y=300)
    tv = ttk.Treeview(frame, columns=(1, 2, 3), show="headings", height="5")
    tv.pack()
    match chosen:
        case "table1":
            tv.heading(1, text="№")
            tv.heading(2, text="adress")
            tv.heading(3, text="FIO")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table2":
            tv.heading(1, text="Category")
            tv.heading(2, text="Minimum аge")
            tv.heading(3, text="Maximum аge")

            for i in rows:
                tv.insert('', 'end', values=i)
        case "table3":
            tv.heading(1, text="№")
            tv.heading(2, text="Category")
            tv.heading(3, text="Teacher")

            for i in rows:
                tv.insert('', 'end', values=i)
    con.commit()
    con.close()

def generate_report():
    global local_state, local_state_rows, local_state_sort
    report_window = Toplevel(root)
    report_window.geometry("400x300")
    report_window.title("Отчет")

    report_text = Text(report_window)
    report_text.pack(expand=True, fill=BOTH)

    def create_report_text():
        report_text.delete(1.0, END)

        if local_state == "search":
            report_text.insert(END, f"Строка для поиска: {sel_entry.get()}")
        elif local_state == "sort":
            if local_state_sort == "desc":
                report_text.insert(END, f"Сортировка по убыванию столбца {combo_out3}")
            else:
                report_text.insert(END, f"Сортировка по возрастанию столбца {combo_out3}")
        elif local_state == "no":
            report_text.insert(END, f"Поиск или сортировка не проводилась")

        report_text.insert(END, "\n\n")

        con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM {chosen}')
        if local_state_rows == "no":
            rows = cursor.fetchall()
        else:
            rows = local_state_rows

        report_text.insert(END, f"Таблица: {chosen}:\n")

        headers = [description[0] for description in cursor.description]
        table_data = [headers] + list(rows)

        report_text.insert(END, tabulate.tabulate(table_data, headers="firstrow", tablefmt="grid"))

        con.close()

    create_report_text()

local_state_rows = None
local_state_sort = None
root = Tk()
root.geometry("900x600")
root.title("База данных")
con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
cursor = con.cursor()

table1_button = Button(root, text = "Table1", command=table1)
table1_button.place(x=10, y=10)

table2_button = Button(root, text = "Table2", command=table2)
table2_button.place(x=110, y=10)

table3_button = Button(root, text = "Table3", command=table3)
table3_button.place(x=210, y=10)

add_record_button = Button(root, text="Добавить", command=add_record)
add_record_button.place(x=380, y=70)

delete_record_button = Button(root, text="Удалить", command=delete_record)
delete_record_button.place(x=0, y=110)

update_record_button = Button(root, text="Изменить", command=update_record)
update_record_button.place(x=0, y=150)

select_button = Button(root, text="Найти", command=select_record)
select_button.place(x=0, y=190)

sort_button = Button(root, text="Сортировать", command=sort_record)
sort_button.place(x=0, y=230)

report_button = Button(root, text="Отчет", command=generate_report)
report_button.place(x=0, y=270)

table1()
text_label1 = Label(root, text="из")
text_label1.place(x=60, y=115)
text_label3 = Label(root, text=" где")
text_label3.place(x=120, y=115)
text_label4 = Label(root, text="равен")
text_label4.place(x=300, y=115)
text_label5 = Label(root, text="на")
text_label5.place(x=230, y=150)
text_label6 = Label(root, text=" где")
text_label6.place(x=370, y=150)
text_label7 = Label(root, text="равен")
text_label7.place(x=550, y=150)
text_label8 = Label(root, text="записи из")
text_label8.place(x=50, y=190)
text_label9 = Label(root, text="где")
text_label9.place(x=150, y=190)
text_label10 = Label(root, text="равен")
text_label10.place(x=330, y=190)
del_entry = Entry(root, width=20)
del_entry.place(x=350, y=115)
upd_entry1 = Entry(root, width=20)
upd_entry1.place(x=600, y=150)
upd_entry2 = Entry(root, width=20)
upd_entry2.place(x=250, y=150)
sel_entry = Entry(root, width=20)
sel_entry.place(x=370, y=190)
sort_entry = Entry(root, width=20)
sort_entry.place(x=100, y=230)
root.mainloop()