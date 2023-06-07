def rabin_karp_search(pattern, text):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:m])

    for i in range(n - m + 1):
        if pattern_hash == text_hash and pattern == text[i:i + m]:
            return i

        if i < n - m:
            text_hash = rehash(text, text_hash, i, m)

    return -1


def hash(string):
    # Простой хеш-алгоритм
    # Можно заменить на более сложный хеш-алгоритм для уменьшения вероятности коллизий
    return sum(ord(c) for c in string)


def rehash(string, prev_hash, index, length):
    old_char_hash = ord(string[index])
    new_char_hash = ord(string[index + length])
    new_hash = prev_hash - old_char_hash + new_char_hash
    return new_hash


# Пример использования
text = "ABACADABRAC"
pattern = "ABRA"

index = rabin_karp_search(pattern, text)

if index != -1:
    print("Образец найден в позиции:", index)
else:
    print("Образец не найден")
