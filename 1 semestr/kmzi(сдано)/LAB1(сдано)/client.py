from cryptography.fernet import Fernet
import os
import random
from socket import *

client = socket(
    AF_INET, SOCK_STREAM #Параметры подключения
)

client.connect(
    ('100.70.62.220', 7000)  #Адрес и сокет куда подключаться
)

password = b'mc0OEsmkyMW_sAtNuyy1CnRfuErJmvllp-6_Gv0bfMY='  #паорль

def send():
    message = input("Введите текст сообещния: ")
    client.send(message.encode('utf-8'))


def recive():
    print("Ожидание сообщения")
    msg = client.recv( 8192 ).decode('utf-8')
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
    i, j = 0, 0
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
    print("Waiting server response...")
    start_message = "START"
    respond = ""
    client.send(start_message.encode('utf-8'))
    while respond != "READY":
        respond = client.recv( 8192 ).decode('utf-8')
    print("Server responded")
    p = generate_random_prime()  #случайное число p
    g = generate_random_number() #случайное число g
    x = generate_random_number() #случайное число x
    while x == g:
        x = generate_random_number()
    r = (g ^ x) % p  #вычисление r
    #Открытым ключом являются r, g и p. И g, и p можно сделать общими для группы пользователей . Закрытым ключом является x.
    print("Generating key")
    r = str(r).encode('utf-8')
    client.send(r)
    f = Fernet(password)
    rec_num = ""
    while rec_num == "" :
        rec_num = client.recv( 8192 )          #получение числа от сервера
    print("Random number receved")   
    rec_num = f.decrypt(rec_num)
    print(rec_num)
    print("Sending number to server")
    rec_num = f.encrypt(rec_num)      #отправка его же серверу
    client.send(rec_num)
    d_seans_key = ""
    while d_seans_key == "":
        d_seans_key = client.recv( 8192 )     #получение зашифрованного сеансового ключа
    print("Seans key recieved, decrypting")
    seans_key = f.decrypt(d_seans_key)
    seans_key = seans_key[sliceing]
    print("Seans key decrypted")
    print("Encrypting string, sending to server")
    f = Fernet(seans_key)     #шифруем сообщение сеансовым ключем
    str1 = b"aboba send"
    encrypted_string = f.encrypt(str1)
    client.send(encrypted_string)
    str1 = "aboba send"   #люблю костыли)
    enc_string1, enc_string2 = "", ""
    while enc_string1 == "" and enc_string2 == "":
        enc_string1 = client.recv( 8192 )
        enc_string2 = client.recv( 8192 )
    print("String received, decoding")
    string1 = str(f.decrypt(enc_string1))
    string1 = string1[sliceing]
    if string1 == str1:
        print("String coincided")    #расшифровка первой строки и проверка, совпали ои они
    string2 = str(f.decrypt(enc_string2)) #расшифровка и повторная шифровка второй строки для отправки на сервер
    string2 = string2[sliceing].encode('utf-8')
    encrypted_string2 = f.encrypt(string2)
    client.send(encrypted_string2)
    print("Messages encrypted with RC4")
    seans_key = str(seans_key)[sliceing]
    print("Сеансовый ключ: ",seans_key)

    while True:
        task = input("Выберете действие: \n\t 1-отправить сообщение\n\t 2-получить сообщение\n")
        match task:
            case "1":
                plaintext = input("Write message: ")
                encrypted = rc4(seans_key, plaintext)
                print("Отправленное сообщение ", encrypted)
                client.send(encrypted.encode('utf-8'))
            case "2":
                encrypted = str(client.recv( 8192 ).decode('utf-8'))
                print("Полученное сообщение: ", encrypted)
                decrypted = rc4(seans_key, encrypted)
                print("Расшифрованный текст:", decrypted)
            case "e":
                client.close()
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
    task = input("Выберете действие:\n\t 1-отправить сообщение\n\t 2-получить сообщение\n\t 3-лаба\n")
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
            client.close()
            os.system("cls")
            break
        case _:
            print("Нет такого лействия")