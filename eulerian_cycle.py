def find_eulerian_cycle(graph):
    num_vertices = len(graph)
    cycle = []
    stack = []
    current_vertex = 0  # Начинаем с вершины 0

    while True:
        cycle.append(current_vertex)
        # Поиск непосещенных смежных вершин
        unvisited_neighbors = [neighbor for neighbor in range(num_vertices) if graph[current_vertex][neighbor] > 0]

        if unvisited_neighbors:
            # Добавляем текущую вершину в стек и выбираем случайного смежного непосещенного соседа
            stack.append(current_vertex)
            next_vertex = unvisited_neighbors[0]

            # Удаляем ребро между текущей вершиной и выбранной вершиной
            graph[current_vertex][next_vertex] -= 1
            graph[next_vertex][current_vertex] -= 1

            # Переходим к выбранной вершине
            current_vertex = next_vertex
        elif stack:
            # Если у текущей вершины нет непосещенных смежных вершин, возвращаемся к предыдущей вершине из стека
            current_vertex = stack.pop()
        else:
            # Если стек пуст, завершаем цикл
            break

    return cycle
# Пример графа, заданного матрицей смежности
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

eulerian_cycle = find_eulerian_cycle(adjacency_matrix)
print("Эйлеров цикл:", eulerian_cycle)
