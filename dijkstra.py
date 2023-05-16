def dijkstra(graph, start_vertex):
    # Инициализация начальных значений
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    visited = set()

    while len(visited) < len(graph):
        # Находим вершину с минимальным расстоянием
        min_distance = float('inf')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Посещаем выбранную вершину
        visited.add(min_vertex)

        # Обновляем расстояния до смежных вершин
        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
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
shortest_distances = dijkstra(graph, start_vertex)
print(shortest_distances)
