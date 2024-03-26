def count_diff(word1, word2):
    if len(word1) != len(word2):
        raise ValueError("Строки должны иметь одинаковую длину")

    # Инициализируем счетчик отличающихся букв
    count = 0

    # Проходим по символам в обеих строках и сравниваем их
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count