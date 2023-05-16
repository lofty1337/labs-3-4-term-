def bellman_ford(graph, start_vertex):
    # Инициализация начальных значений
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0

    # Проходимся по всем вершинам графа
    for _ in range(len(graph) - 1):
        # Проходимся по всем ребрам графа
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                # Обновляем расстояние до смежной вершины
                new_distance = distances[vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 4, 'C': 3}
}

start_vertex = 'A'
shortest_distances = bellman_ford(graph, start_vertex)
print(shortest_distances)
