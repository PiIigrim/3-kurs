def message_to_bits(message):
    bits = ''.join(format(ord(char), '08b') for char in message)
    return bits

# Пример использования
message = "Hello, world!"
bit_sequence = message_to_bits(message)
print("Message in bits:", bit_sequence)