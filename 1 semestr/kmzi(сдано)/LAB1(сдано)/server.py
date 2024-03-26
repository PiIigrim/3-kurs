from cryptography.fernet import Fernet
import os
import random
from socket import *

server = socket(
    AF_INET, SOCK_STREAM  #параметры подключения
)

server.bind(
    ('100.70.62.220', 7000)  #адресс и сокет сервера
)

server.listen(2)  #количество подключений

print("SERVER IS WORKING\n")
user, addr = server.accept()  #после подключения, выполнять далее
print(f"CONNECTED:\n\t{user}\n\t{addr}\n")

user.send('Connected successful!'.encode('utf-8'))  #отправить сообщение

password = b'mc0OEsmkyMW_sAtNuyy1CnRfuErJmvllp-6_Gv0bfMY='  #паорль

def send():
    message = input("Введите текст сообещния: ")
    user.send(message.encode('utf-8'))

def recive():
    print("Ожидание сообщения")
    msg = user.recv( 8192 ).decode('utf-8')
    print(f'SERVER MESSAGE:\n\t{msg}')

def rc4(key, plaintext):
    # Инициализация S-Box и массива ключа K
    S = list(range(256))
    K = [ord(key[i % len(key)]) for i in range(256)]
    
    # Перемешивание S-Box
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Генерация ключевого потока и шифрование/дешифрование
    i = 0
    j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_byte = S[(S[i] + S[j]) % 256]
        ciphertext.append(chr(ord(char) ^ key_byte))
    
    return ''.join(ciphertext)

def main():
    sliceing = slice(2, -1)
    print("Witing for client")
    msg = ""
    while msg !="START":
        msg = user.recv( 8192 ).decode('utf-8')
    message = "READY"
    user.send(message.encode('utf-8'))
    print("Clinet ready")
    f = Fernet(password)
    msg = ""
    while msg == "":
        msg = user.recv( 8192 )  #получение ключа от клиента
    print("Key recieved")
    print("Sending random encoded number")
    R = random.randint(1, 50)
    R1 = str(R).encode('utf-8')
    R_enc = f.encrypt(R1)
    print("Sending number to client")
    user.send(R_enc)
    R_rec = ""
    while R_rec == "" :
        R_rec = user.recv( 8192 )
    print("Number received, decoding")
    R2 = f.decrypt(R_rec)
    if int(R2) == R:
        print("Number coincided")
    print("generating seans key")
    seans_key = Fernet.generate_key()    #тоже самое что у клиента
    seans_key1 = str(seans_key)
    print("Encrypting seans key, sending to client")
    byte_s_key = seans_key1.encode('utf-8')
    encrypted_seans_key = f.encrypt(byte_s_key)   #шифровка и отправка сеансового ключа
    user.send(encrypted_seans_key)
    encrypted_string = ""
    while encrypted_string == "":
        encrypted_string = user.recv( 8192 )
    print("Encrypted string received")
    f = Fernet(seans_key)
    decrypted_string = str(f.decrypt(encrypted_string))  #расшифровка строки клиента
    decrypted_string = decrypted_string[sliceing].encode('utf-8')
    print("String decoded")
    print("Encoding both strings, sending to client")
    string2 = b"aboba recive"
    encrypted_string_again = f.encrypt(decrypted_string)  #шифруем строки сервера и клиента
    encrypted_string2 = f.encrypt(string2)
    string2 = "aboba recive"
    user.send(encrypted_string_again)
    user.send(encrypted_string2)
    enc_ver_string2 = ""  #получение строки от клиента для валидации
    while enc_ver_string2 == "":
        enc_ver_string2 = user.recv( 8192 )
    ver_string2 = str(f.decrypt(enc_ver_string2))
    ver_string2 = ver_string2[sliceing]
    print("String received, decoding")
    if ver_string2 == string2:
        print("String coincided")
    print("Messages encrypted with RC4")
    seans_key = str(seans_key)[sliceing]
    print("Сеансовый ключ: ",seans_key)

    while True:
        task = input("Выберете действие: \n\t 1-отправить соо,щение\n\t 2-получить сообщение\n")
        match task:
            case "1":
                plaintext = input("Write message: ")
                encrypted = rc4(seans_key, plaintext)
                print("Зашифрованное сообщение ", encrypted)
                user.send(encrypted.encode('utf-8'))
            case "2":
                encrypted = str(user.recv( 8192 ).decode('utf-8'))
                print("Полученное сообщение: ", encrypted)
                decrypted = rc4(seans_key, encrypted)
                print("Расшифрованный текст:", decrypted)
            case "e":
                server.close()
                os.system("cls")
                break
            case _:
                print("Нет такого лействия")


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_prime():
    while True:
        num = random.randint(10, 100) 
        if is_prime(num):
            return num


def generate_random_number():
    prime = generate_random_prime()
    num = random.randint(1, prime - 1)  
    return num

def test():
    key = "SecretKey"
    plaintext = "Hello, RC4!"

    encrypted = rc4(key, plaintext)
    print("Зашифрованный текст:", encrypted)

    decrypted = rc4(key, encrypted)
    print("Расшифрованный текст:", decrypted)


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
            test()
        case "e":
            server.close()
            os.system("cls")
            break
        case _:
            print("Нет такого лействия")