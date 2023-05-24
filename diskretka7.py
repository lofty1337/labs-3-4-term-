from collections import deque, defaultdict
import heapq
import random
import time

def generate_sparse_graph(num_vertices):
    G = {}
    for i in range(num_vertices):
        G[i] = defaultdict(int)

    # Добавляем подграф K_7
    k7_nodes = random.sample(range(num_vertices), 7)
    for n1 in k7_nodes:
        for n2 in k7_nodes:
            if n1 < n2:
                G[n1][n2] = 1
                G[n2][n1] = 1

    # Добавляем ребра до достижимых вершин для каждой вершины
    for i in range(num_vertices):
        while len(G[i]) < 10:
            neighbor = random.randint(0, num_vertices-1)
            if neighbor != i:
                G[i][neighbor] = 1
                G[neighbor][i] = 1

    return G

def bfs_shortest_path(graph, source):
    distances = {node: float('inf') for node in graph.keys()}
    distances[source] = 0

    queue = deque([source])

    iterations = 0

    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            iterations += 1
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
                iterations += 1

    return distances, iterations

def dijkstra_shortest_path(graph, source):
    distances = {node: float('inf') for node in graph.keys()}
    distances[source] = 0

    pq = [(0, source)]

    iterations = 0

    while pq:
        iterations += 1
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            iterations += 1
            continue

        for neighbor, weight in graph[curr_node].items():
            new_dist = curr_dist + weight
            iterations += 1
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                iterations += 1

    return distances, iterations

def test_graph(num_vertices):
    # Генерируем разреженный граф
    graph = generate_sparse_graph(num_vertices)

    # Выбираем случайную вершину в качестве источника
    source_node = random.choice(list(graph.keys()))

    # Вычисляем кратчайшие пути с использованием BFS алгоритма
    start_time = time.time()
    bfs_distances, bfs_iterations = bfs_shortest_path(graph, source_node)
    bfs_execution_time = time.time() - start_time

    # Вычисляем кратчайшие пути с использованием алгоритма Дейкстры
    start_time = time.time()
    dijkstra_distances, dijkstra_iterations = dijkstra_shortest_path(graph, source_node)
    dijkstra_execution_time = time.time() - start_time

    # Выводим результаты

    print(f"Graph with {num_vertices} vertices:")
    print(f"Source node: {source_node}")
    print(f"Average degree: {sum(len(neighbors) for neighbors in graph.values()) / num_vertices:.2f}")
    print()

    print("BFS:")
    print(f"Iterations: {bfs_iterations}")
    print(f"Execution time: {bfs_execution_time:.4f} seconds")
    print()

    print("Dijkstra:")
    print(f"Iterations: {dijkstra_iterations}")
    print(f"Execution time: {dijkstra_execution_time:.4f} seconds")
    print()

# Задаем список числа вершин для тестирования
num_vertices_list = [12000, 32000, 80000, 200000, 500000]

# Тестируем каждое число вершин
for num_vertices in num_vertices_list:
    test_graph(num_vertices)
    print('=' * 50)
