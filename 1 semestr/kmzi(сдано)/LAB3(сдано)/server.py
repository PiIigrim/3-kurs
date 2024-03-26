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


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def find_a_b_for_equation(p, q):
    gcd, a, b = extended_gcd(p, q)
    return a, b

def message_to_bits(num, bit_length=8):
    if num >= 0:
        bits = bin(num)[2:].zfill(bit_length)
    else:
        # Преобразование отрицательного числа в дополнительный код
        num = abs(num)
        bits = bin(num)[2:]
        if len(bits) < bit_length:
            bits = '0' * (bit_length - len(bits)) + bits
        inverted = ''.join('1' if bit == '0' else '0' for bit in bits)
        inverted = inverted[-bit_length:]
        carry = 1
        result = ''
        for bit in inverted[::-1]:
            if bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            elif bit == '1' and carry == 1:
                result = '0' + result
            else:
                result = bit + result
        bits = result
    return bits


def main():
    p = int(user.recv( 8192 ).decode('utf-8'))   
    print("p: ", p)
    q = int(user.recv( 8192 ).decode('utf-8'))
    print("q: ", q)
    n = int(user.recv( 8192 ).decode('utf-8'))
    print("n: ", n)
    m = (user.recv( 8192 ).decode('utf-8'))
    c = int(user.recv( 8192 ).decode('utf-8'))  
    print("c: ", c)

    a, b = find_a_b_for_equation(p, q)

    r = (c * (p + 1) // 4) % p
    s = (c * (q + 1) // 4) % q
    x = (a * p * r + b * q * s) % p
    y = (a * p * r - b * q * s) % q

    m1 = x; m2 = -x; m3 = y; m4 = -y

    m1_bits = message_to_bits(m1)
    m2_bits = message_to_bits(m2)
    m3_bits = message_to_bits(m3)
    m4_bits = message_to_bits(m4)

    half_length_m1 = len(m1_bits) // 2 
    half_length_m2 = len(m2_bits) // 2
    half_length_m3 = len(m3_bits) // 2
    half_length_m4 = len(m4_bits) // 2 

    left_half_m1 = m1_bits[:half_length_m1]
    right_half_m1 = m1_bits[half_length_m1:]

    left_half_m2 = m2_bits[:half_length_m2]
    right_half_m2 = m2_bits[half_length_m2:]

    left_half_m3 = m3_bits[:half_length_m3]
    right_half_m3 = m3_bits[half_length_m3:]

    left_half_m4 = m4_bits[:half_length_m4]
    right_half_m4 = m4_bits[half_length_m4:]

    matching_half = None
    if left_half_m1 == right_half_m1:
        matching_half = left_half_m1
    elif left_half_m2 == right_half_m2:
        matching_half = left_half_m2
    elif left_half_m3 == right_half_m3:
        matching_half = left_half_m3
    elif left_half_m4 == right_half_m4:
        matching_half = left_half_m4

    if matching_half is not None:
        # Преобразование половины в десятичное число
        matching_half_decimal = int(matching_half, 2)

        # Получение ASCII символа для десятичного числа
        message = chr(matching_half_decimal)

        print(f"Decoded Message: {message}")
    else:
        print(f"Decoded Message: {m}")


while True:
    task = input("Выберете действие: \n\t 1-отправить сообщение\n\t 2-получить сообщение\n\t 3-лаба\n")
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
            print("Нет такого действия")

