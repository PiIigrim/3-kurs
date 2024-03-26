from collections import Counter
import re

def count_unique_words(input_file, output_file):
    # Считываем текст из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Преобразуем текст в нижний регистр для учета слов вне зависимости от регистра

    # Используем регулярное выражение для извлечения слов из текста
    words = re.findall(r'\b\w+\b', text)

    # Считаем количество появлений каждого слова
    word_counts = Counter(words)

    unique_sorted_words = sorted(word_counts.items())

    # Записываем уникальные слова и их количество в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in unique_sorted_words:
            file.write(f"{word} {count}\n")

# Пример использования
input_filename = 'leksemes.txt'  # Название вашего файла с текстом
output_filename = 'count.txt'  # Название файла, куда будет записан результат

count_unique_words(input_filename, output_filename)
