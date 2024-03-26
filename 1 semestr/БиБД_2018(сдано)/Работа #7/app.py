from flask import Flask, render_template, request
import mysql.connector as mysql

app = Flask(__name__)

# Функция для получения данных из базы данных
def get_data(table_name):
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    con.close()
    return rows

# Функция для выполнения запроса к базе данных
def execute_query(query):
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="kindergarden")
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    con.close()

@app.route('/')
def index():
    # Переместим запрос данных сюда
    data = get_data('table1')
    return render_template('table1.html', data=data)

@app.route('/table1', methods=['POST', 'GET'])
def table1():
    if request.method == 'POST':
        f_number = request.form.get('f_number')
        f_adress = request.form.get('f_adress')
        f_FIO = request.form.get('f_FIO')

        # Используем функцию execute_query для выполнения запроса
        execute_query(f'INSERT INTO table1 VALUES ({f_number}, "{f_adress}", "{f_FIO}")')

    # Переместим запрос данных сюда
    data = get_data('table1')
    return render_template('table1.html', data=data)

@app.route('/delete_table1', methods=['POST'])
def delete_table1():
    id_to_delete = request.form.get('id_to_delete')

    # Используем функцию execute_query для выполнения запроса
    execute_query(f'DELETE FROM table1 WHERE № = {id_to_delete}')

    data = get_data('table1')
    return render_template('table1.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)