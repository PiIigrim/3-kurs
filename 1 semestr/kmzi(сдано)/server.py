import os
from socket import *

server = socket(
    AF_INET, SOCK_STREAM  #параметры подключения
)

server.bind(
    ('localhost', 7000)  #адресс и сокет сервера
)

server.listen(2)  #количество подключений

print("SERVER IS WORKING\n")
user, addr = server.accept()  #после подключения, выполнять далее
print(f"CONNECTED:\n\t{user}\n\t{addr}\n")

user.send('Connected successful!'.encode('utf-8'))  #отправить сообщение

def send():
    message = input("Введите текст сообещния: ")
    user.send(message.encode('utf-8'))

def recive():
    print("Ожидание сообщения")
    msg = user.recv( 8192 ).decode('utf-8')
    print(f'SERVER MESSAGE:\n\t{msg}')

def main():
    pass

while True:
    task = input("Выберете действие: \n\t 1-отправить соо,щение\n\t 2-получить сообщение\n\t 3-лаба\n")
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
            server.close()
            os.system("cls")
            break
        case _:
            print("Нет такого лействия")

