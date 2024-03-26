from socket import *
import os, msvcrt, datetime

client = socket(
    AF_INET, SOCK_STREAM #Параметры подключения
)
ip = "127.0.0.1"
addr = ""
port = 0
connect = False
while connect == False:
    cmd = input()
    cmd = cmd.split()
    for word in cmd:
            if word == "connect" and cmd[cmd.index(word) + 1] == ip and int(cmd[cmd.index(word) + 2]) == 7000 and cmd.index(word) == 0:
                addr = cmd[cmd.index(word) + 1]
                port = int(cmd[cmd.index(word) + 2])
                server_addr = (addr, port)
                connect = True
                client.connect(
                    (addr, port)  #Адрес и сокет куда подключаться
                )

def send():
    message = ""
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                    print(key.decode('utf-8'),end = '', flush=True)
            except UnicodeDecodeError:
                    pass
            if key == b'\xe0' or key == b'\r':
                print(" ")
                client.send(message.encode('utf-8'))
                time = datetime.datetime.now()
                with open("C:\\work\\AIPOSOZI\\Lab1 - TCP\\log.txt", 'a') as file:
                     file.write(f"[{time}] Строка \"{message}\" отправленна на сервер\n")
                break
            else:
                try:
                    if key == b'I' or key == b'\r':
                         pass
                    else:
                        message += key.decode('utf-8')
                except UnicodeDecodeError:
                    pass


def recive():
    print("Ожидание сообщения")
    msg = client.recv( 1024 ).decode('utf-8')
    time = datetime.datetime.now()
    with open("C:\\work\\AIPOSOZI\\Lab1 - TCP\\log.txt", 'a') as file:
        file.write(f"[{time}] Строка \"{msg}\" полученна от сервера\n")
    print(f'SERVER MESSAGE:\n\t{msg}')


while True:
    task = input("Выберете действие:\n\t 1-отправить сообщение\n\t 2-получить сообщение\n")
    match task:
        case "1":
            send()
        case "2":
            recive()
        case "e":
            client.close()
            os.system("cls")
            break
        case _:
            print("Нет такого действия")