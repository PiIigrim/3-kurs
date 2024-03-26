from socket import *
import os

client = socket(
    AF_INET, SOCK_STREAM #Параметры подключения
)

client.connect(
    ('localhost', 7000)  #Адрес и сокет куда подключаться
)

def send():
    message = input("Введите текст сообещния: ")
    client.send(message.encode('utf-8'))

def recive():
    print("Ожидание сообщения")
    msg = client.recv( 8192 ).decode('utf-8')
    print(f'SERVER MESSAGE:\n\t{msg}')

def main():
    pass

while True:
    task = input("Выберете действие:\n\t 1-отправить сообщение\n\t 2-получить сообщение\n\t 3-лаба\n")
    match task:
        case "1":
            send()
        case "2":
            recive()
        case "3":
            main()
        case "9":
            pass
        case "e":
            client.close()
            os.system("cls")
            break
        case _:
            print("Нет такого лействия")