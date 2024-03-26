from socket import *
import random
import os

client = socket(
    AF_INET, SOCK_STREAM 
)

client.connect(
    ('localhost', 7000) 
)

def send():
    message = input("Введите текст сообещния: ")
    client.send(message.encode('utf-8'))

def recive():
    print("Ожидание сообщения")
    msg = client.recv( 8192 ).decode('utf-8')
    print(f'SERVER MESSAGE:\n\t{msg}')

def message_to_bits(message):
    bits = ''.join(format(ord(char), '08b') for char in message)
    return bits

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not (is_prime(prime) and prime % 4 == 3):
        prime = random.randint(min_value, max_value)
    return prime

def create_n():
    p = generate_prime(30, 10000)
    print("p:", p)
    client.send(str(p).encode('utf-8')) 
    q = generate_prime(30, 10000)
    print("q:", q)
    client.send(str(q).encode('utf-8')) 
    n = p * q
    print("n:", n)
    client.send(str(n).encode('utf-8')) 
    return p, q, n

def main():
    p, q, n = create_n()
    message = input("Введите сообщение для шифровки: ")
    client.send(message.encode('utf-8'))
    m = [ord(char) for char in message]
    m_binary = ''.join(format(char, '08b') for char in m)
    extended_m_binary = m_binary + m_binary
    m = int(extended_m_binary, 2)
    c = (m^2) % n
    client.send(str(c).encode('utf-8')) 

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