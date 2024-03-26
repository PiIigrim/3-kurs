import random

how = int(input("1-по возрастанию, 2-по убыванию: "))
while how != 1 and how != 2:
    print("Naaaahh")
    how = int(input("1-по возрастанию, 2-по убыванию: "))

with open("ССП\\лабы\\text.txt", "w") as file:
    num_num = random.randint(1, 1000000)
    file.write(f'Generates {num_num} random numbers' + '\n')
    for _ in range(num_num):
        random_num = random.randint(1, 1000)
        file.write(str(random_num) + '\n')

print(f'Generates {num_num} random numbers')

with open("ССП\\лабы\\text.txt", "r") as input_file:
    next(input_file)
    values = [int(line.strip()) for line in input_file]
    if how == 1:
        sorted_values = sorted(values)
    elif how == 2:
        sorted_values = sorted(values, reverse=True)

with open("ССП\\лабы\\output.txt", "w") as output_file:
    for value in sorted_values:
        output_file.write(str(value) + '\n')
        
print("Values sorted")