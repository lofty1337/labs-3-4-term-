from collections import deque

def bfs(A, s, d):
    q = deque([s])
    d[s] = True
    component = [s]
    while q:
        v = q.popleft()
        for u in A[v]:
            if not d[u]:
                d[u] = True
                component.append(u)
                q.append(u)
    return component

def find_components(graph):
    n = len(graph)
    d = [False] * n
    components = []
    for v in range(n):
        if not d[v]:
            component = bfs(graph, v, d)
            components.append(component)
    return components

# Пример использования
graph = [[1, 2], [0], [0], [4], [3]]
components = find_components(graph)
print(f"Количество компонент связности: {len(components)}")
for i, component in enumerate(components):
    print(f"Компонента {i+1}: {component}")
