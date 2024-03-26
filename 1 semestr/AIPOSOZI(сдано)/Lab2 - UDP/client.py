from socket import *
import os, msvcrt, datetime

client = socket(AF_INET, SOCK_DGRAM) 
ip = "127.0.0.1"
addr = ""
port = 0
connect = False

while not connect:
    cmd = input()
    cmd = cmd.split()
    for word in cmd:
        if word == "connect" and cmd[cmd.index(word) + 1] == ip and int(cmd[cmd.index(word) + 2]) == 7000 and cmd.index(word) == 0:
            addr = cmd[cmd.index(word) + 1]
            port = int(cmd[cmd.index(word) + 2])
            server_addr = (addr, port)
            connect = True

def send():
    print("Введите сообщение: ")
    message = ""
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                print(key.decode('utf-8'), end='', flush=True)
            except UnicodeDecodeError:
                pass
            if key == b'\xe0' or key == b'\r':
                print(" ")
                message_bytes = message.encode('utf-8')
                client.sendto(message_bytes, server_addr)
                time = datetime.datetime.now()
                with open("C:\\work\\AIPOSOZI\\Lab2 - UDP\\log.txt", 'a') as file:
                    file.write(f"[{time}] Строка \"{message}\" отправлена на сервер\n")
                break
            else:
                try:
                    if key == b'I' or key == b'\r':
                        pass
                    else:
                        message += key.decode('utf-8')
                except UnicodeDecodeError:
                    pass

def receive():
    print("Ожидание сообщения")
    msg, sender_addr = client.recvfrom(1024)
    msg = msg.decode('utf-8')
    time = datetime.datetime.now()
    with open("C:\\work\\AIPOSOZI\\Lab2 - UDP\\log.txt", 'a') as file:
        file.write(f"[{time}] Строка \"{msg}\" получена от сервера\n")
    print(f'SERVER MESSAGE:\n\t{msg}')

while True:
    task = input("Выберете действие:\n\t 1-отправить сообщение\n\t 2-получить сообщение\n")
    match task:
        case "1":
            send()
        case "2":
            receive()
        case "e":
            client.close()
            os.system("cls")
            break
        case _:
            print("Нет такого действия")