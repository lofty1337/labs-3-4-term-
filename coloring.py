def greedy_coloring(graph):
    colors = {}  # Словарь для хранения цветов вершин

    # Проходим по каждой вершине графа
    for vertex in graph:
        used_colors = set()  # Множество цветов, использованных соседними вершинами

        # Проверяем цвета соседних вершин
        for neighbor in graph[vertex]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        # Находим минимальный доступный цвет
        for color in range(len(graph)):
            if color not in used_colors:
                colors[vertex] = color
                break

    return colors


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = greedy_coloring(graph)
print(colors)
