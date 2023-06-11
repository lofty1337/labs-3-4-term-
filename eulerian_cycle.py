def find_eulerian_cycle(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    eulerian_cycle = []

    def dfs(vertex):
        for neighbor in range(num_vertices):
            if adjacency_matrix[vertex][neighbor] > 0:
                adjacency_matrix[vertex][neighbor] -= 1
                adjacency_matrix[neighbor][vertex] -= 1
                dfs(neighbor)

        eulerian_cycle.append(vertex)

    dfs(0)

    if len(eulerian_cycle) != num_vertices + 1:
        return []

    return eulerian_cycle[::-1]


# Пример использования
adjacency_matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]
]

eulerian_cycle = find_eulerian_cycle(adjacency_matrix)

if eulerian_cycle:
    print("Эйлеров цикл найден:")
    print(eulerian_cycle)
else:
    print("Эйлеров цикл не найден")
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

eulerian_cycle = find_eulerian_cycle(adjacency_matrix)

if eulerian_cycle:
    print("Эйлеров цикл найден:")
    print(eulerian_cycle)
else:
    print("Эйлеров цикл не найден")
