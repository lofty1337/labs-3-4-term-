def prim(graph):
    # Создаем пустое минимальное покрывающее дерево и множество вершин, уже включенных в дерево
    minimum_spanning_tree = {}
    visited = set()

    # Выбираем произвольную начальную вершину
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None

        # Поиск ребра минимального веса, которое соединяет посещенную вершину с непосещенной вершиной
        for vertex in visited:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)

        # Добавляем найденное ребро в минимальное покрывающее дерево
        if min_edge:
            vertex, neighbor = min_edge
            minimum_spanning_tree[vertex] = {neighbor: min_weight}
            visited.add(neighbor)

    return minimum_spanning_tree

# Пример использования
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

minimum_spanning_tree = prim(graph)
print(minimum_spanning_tree)
