from socket import *
import os

server = socket(
    AF_INET, SOCK_STREAM  #параметры подключения
)

server.bind(
    ('127.0.0.1', 7000)  #адресс и сокет сервера
)

server.listen(5)  #количество подключений
print("SERVER WORKING")
user, addr = server.accept()  #после подключения, выполнять далее
print(f"CONNECTED:\n\t{user}\n\t{addr}\n")

#user.send('Connected successful!'.encode('utf-8'))  #отправить сообщение
def send():
    message = input("Введите текст сообещния: ")
    user.send(message.encode('utf-8'))

def recive():
    print("Ожидание сообщения")
    msg = user.recv( 1024 ).decode('utf-8')
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
        print("File not find")
    for word in words:
        if string.lower() in word.lower():
            number += 1
            print("Word found: ", word)
            found = True
    print("Number of words found: ", number)
    if found == False:
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
            recive()
        case "e":
            server.close()
            os.system("cls")
            break
        case "a":
            server.close()
            break
        case _:
            print("Нет такого лействия")