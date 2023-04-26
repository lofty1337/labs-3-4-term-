def kosaraju(graph):
    # первый обход в глубину для заполнения списка посещенных вершин
    visited = set()
    order = []
    for v in graph:
        if v not in visited:
            dfs_visit(v, visited, order, graph)

    # транспонирование графа
    transpose_graph = get_transpose(graph)

    # второй обход в глубину для нахождения сильно связных компонент
    visited = set()
    scc_list = []
    while order:
        v = order.pop()
        if v not in visited:
            scc = set()
            dfs_scc(v, visited, scc, transpose_graph)
            scc_list.append(scc)

    return scc_list


def dfs_visit(v, visited, order, graph):
    visited.add(v)
    for u in graph.get(v, []):
        if u not in visited:
            dfs_visit(u, visited, order, graph)
    order.append(v)


def dfs_scc(v, visited, scc, graph):
    visited.add(v)
    scc.add(v)
    for u in graph.get(v, []):
        if u not in visited:
            dfs_scc(u, visited, scc, graph)


def get_transpose(graph):
    transpose_graph = {v: set() for v in graph}
    for v in graph:
        for u in graph.get(v, []):
            transpose_graph[u].add(v)
    return transpose_graph

graph = {
    0: {1},
    1: {2},
    2: {0, 3},
    3: {4},
    4: {3}
}
scc_list = kosaraju(graph)
print(scc_list)
