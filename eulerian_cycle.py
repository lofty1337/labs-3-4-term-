def find_eulerian_cycle(adjacency_matrix):
    n = len(adjacency_matrix)
    stack = [0]  # Стек для обхода
    path = []  # Результирующий путь

    while stack:
        v = stack[-1]  # Вершина из стека
        has_unvisited_neighbour = False

        for u in range(n):
            if adjacency_matrix[v][u] > 0:
                stack.append(u)  # Добавляем смежную вершину в стек
                adjacency_matrix[v][u] -= 1  # Удаляем ребро из матрицы смежности
                adjacency_matrix[u][v] -= 1
                has_unvisited_neighbour = True
                break

        if not has_unvisited_neighbour:
            path.append(stack.pop())  # Добавляем вершину в результирующий путь

    return path[::-1]  # Инвертируем путь для получения эйлерова цикла


adjacency_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

eulerian_cycle = find_eulerian_cycle(adjacency_matrix)

if eulerian_cycle is not None:
    print("Эйлеров цикл:", eulerian_cycle)
else:
    print("Граф не содержит эйлерова цикла.")
