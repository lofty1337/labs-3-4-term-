def boyer_moore_horspool_search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)

    if pattern_length > text_length:
        return -1

    skip_table = create_skip_table(pattern)

    i = pattern_length - 1
    while i < text_length:
        j = pattern_length - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1

        if j == -1:
            return i + 1

        i += skip_table.get(text[i], pattern_length)

    return -1


def create_skip_table(pattern):
    skip_table = {}

    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        skip_table[pattern[i]] = pattern_length - 1 - i

    return skip_table


# Пример использования
text = "ABACADABRAC"
pattern = "ABRA"

index = boyer_moore_horspool_search(pattern, text)

if index != -1:
    print("Образец найден в позиции:", index)
else:
    print("Образец не найден")
