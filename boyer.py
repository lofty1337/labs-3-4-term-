def generate_bad_character_table(pattern):
    table = {}
    m = len(pattern)

    for i in range(m - 1):
        table[pattern[i]] = m - i - 1

    return table


def generate_good_suffix_table(pattern):
    table = []
    m = len(pattern)
    last_prefix_position = m

    for i in range(m - 1, -1, -1):
        if is_prefix(pattern, i + 1):
            last_prefix_position = i + 1

        table.append(last_prefix_position - i + m - 1)

    for i in range(0, m - 1):
        length = suffix_length(pattern, i)
        table[length] = m - 1 - i + length

    return table


def is_prefix(pattern, p):
    m = len(pattern)

    for i in range(p, m):
        if pattern[i] != pattern[i - p]:
            return False

    return True


def suffix_length(pattern, p):
    m = len(pattern)
    length = 0

    while p >= 0 and pattern[p] == pattern[m - 1 - length]:
        length += 1
        p -= 1

    return length


def search(pattern, text):
    n = len(text)
    m = len(pattern)
    bad_character_table = generate_bad_character_table(pattern)
    good_suffix_table = generate_good_suffix_table(pattern)
    result = []

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            result.append(i)
            i += good_suffix_table[0]
        else:
            bad_character_shift = bad_character_table.get(text[i + j], m)
            good_suffix_shift = good_suffix_table[j]

            i += max(bad_character_shift, good_suffix_shift)

    return result


# Пример использования
text = "ABACADABRAC"
pattern = "ABRA"

matches = search(pattern, text)

if len(matches) > 0:
    print("Образец найден в следующих позициях:")
    print(matches)
else:
    print("Образец не найден")
