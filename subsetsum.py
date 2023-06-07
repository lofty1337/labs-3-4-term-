def subset_sum_greedy(numbers, target_sum):
    numbers.sort(reverse=True)  # Сортируем числа в порядке убывания

    subset = []  # Инициализируем пустое подмножество

    for num in numbers:
        if num <= target_sum:
            subset.append(num)
            target_sum -= num

    if target_sum == 0:
        return subset  # Если удалось найти подмножество с нужной суммой, возвращаем его
    else:
        return None  # Иначе возвращаем None, такое подмножество невозможно


# Пример использования
numbers = [3, 1, 7, 4, 2, 8]  # Числа для составления подмножества
target_sum = 10  # Целевая сумма

result = subset_sum_greedy(numbers, target_sum)

if result is not None:
    print(f"Подмножество с суммой {target_sum} найдено: {result}")
else:
    print(f"Невозможно найти подмножество с суммой {target_sum}")
