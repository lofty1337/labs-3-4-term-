def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m  # Создаем список pi с нулевыми значениями
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]  # Возвращаемся к предыдущему префиксу

        if pattern[k] == pattern[q]:
            k += 1

        pi[q] = k  # Записываем длину наибольшего префикса, который является суффиксом

    return pi


def search(pattern, text):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)  # Вычисляем префикс-функцию для образца
    q = 0  # Текущий индекс в образце
    result = []  # Список для хранения позиций, где найден образец

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]  # Возвращаемся к предыдущему префиксу

        if pattern[q] == text[i]:
            q += 1

        if q == m:
            result.append(i - m + 1)  # Образец найден в позиции i-m+1
            q = pi[q - 1]  # Продолжаем поиск следующих вхождений образца

    return result


# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABC"

matches = search(pattern, text)

if len(matches) > 0:
    print("Образец найден в следующих позициях:")
    print(matches)
else:
    print("Образец не найден")
