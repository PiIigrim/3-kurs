from socket import *
import os

server = socket(AF_INET, SOCK_DGRAM) 
host = '0.0.0.0'
port = 7000
server.bind((host, port))  
print("SERVER WORKING")
print(f"Сервер слушает на {host}:{port}")

while True:
    data, addr = server.recvfrom(1024)  
    data = data.decode('utf-8')
    print(f"CONNECTED:\n\t{addr}\n")

    def send():
        message = input("Введите текст сообщения: ")
        server.sendto(message.encode('utf-8'), addr)

    def receive():
        print("Ожидание сообщения")
        msg, _ = server.recvfrom(1024)
        msg = msg.decode('utf-8')
        print(f'SERVER MESSAGE:\n\t{msg}')
        msg = msg.split(" ")
        for word in msg:
            if word == "find" and len(msg) - msg.index(word) >= 3:
                find(msg[msg.index(word) + 1], msg[msg.index(word) + 2])

    end = False

    def find(string, name):
        global end
        end = False
        found = False
        number = 0
        try:
            with open(name, 'r') as file:
                words = file.read().split()
        except FileNotFoundError:
            print("File not found")
        for word in words:
            if string.lower() in word.lower():
                number += 1
                print("Word found:", word)
                found = True
        print("Number of words found:", number)
        if not found:
            end = True
            print("Word not found, end of connection")

    while True:
        if end == True:
            task = "a"
        else:
            task = input("Выберете действие: \n\t1-отправить сообщение\n\t2-получить сообщение\n")
        match task:
            case "1":
                send()
            case "2":
                receive()
            case "e":
                server.close()
                os.system("cls")
                break
            case "a":
                server.close()
                break
            case _:
                print("Нет такого лействия")