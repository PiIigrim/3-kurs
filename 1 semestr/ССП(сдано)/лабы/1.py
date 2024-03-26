import random
from datetime import datetime


def task_1():
    print("-----------------------------------")
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    numbers = [random.uniform(0, 100) for _ in range(12)]
    for i in range(12):
        print(months[i], ":", numbers[i])
    avarage = sum(numbers)/12
    print("-----------------------------------")
    print("Среднее: ", avarage)
    print("-----------------------------------")


def task_2():
    print("-----------------------------------")
    dates = []
    for _ in range(10):
        Year = random.randint(1000, 2500)
        Month = random.randint(1, 12)
        Day = random.randint(1,28)
        date = datetime(Year, Month, Day)
        dates.append(date)
    for date in dates:
        print(date.strftime("%d %B %Y"))
    print("-----------------------------------")


def task_3():
    print("-----------------------------------")
    letters = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', " "]
    number = int(input("Сколько символов вывести: "))
    for _ in range(number):
        print(random.choice(letters), end='')
    print("")
    print("-----------------------------------")


def task_4():
    print("-----------------------------------")
    string = "создать объект типа стринг и проинициализировать его текстовой строкой определить количество гласных пробелов и общее количество букв"
    vowels = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я"]
    print("Введенная строка: ", string)
    print("Количество гласных : ", sum(string.count(vowels) for vowels in vowels))
    print("Количество пробелов : ", string.count(" "))
    print("Общее количесво букв: ", len([letters for letters in string if letters.isalpha()]))
    print("-----------------------------------")


def task_5():
    print("-----------------------------------")
    text = input("Введите текстовую строку: ")
    string_array = [text]
    delimiter = input("Введите разделитель: ")
    extracted_strings = string_array[0].split(delimiter)
    print("Извлеченные строки:")
    for string in extracted_strings:
        print(string)
    print(string_array)
    print("-----------------------------------")


while(True):
    task = input("Введите номер задания: ")
    match task:
        case "1":
            task_1()
        case "2":
            task_2()
        case "3":
            task_3()
        case "4":
            task_4()
        case "5":
            task_5()
        case "e":
            break
        case _:
            print("Такого задания нет")