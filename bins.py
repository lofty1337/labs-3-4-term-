def first_fit_decreasing(items, bin_capacity):
    items = sorted(items, reverse=True)  # Сортируем предметы в порядке убывания размера
    bins = []  # Список ящиков

    for item in items:
        # Пытаемся разместить предмет в существующем ящике
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                break
        else:
            # Если предмет не помещается ни в один существующий ящик, создаем новый ящик
            bins.append([item])

    return bins


# Пример использования
items = [4, 8, 1, 3, 2, 7, 6]  # Размеры предметов
bin_capacity = 10  # Вместимость ящиков

result = first_fit_decreasing(items, bin_capacity)
for i, bin in enumerate(result):
    print(f"Ящик {i + 1}: {bin}")
