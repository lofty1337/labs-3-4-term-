import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst = []
        for i in range(1, self.V):
            mst.append((parent[i], i, self.graph[i][parent[i]]))

        return mst


# Пример использования
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
minimum_spanning_tree = g.prim()

print("Минимальное покрывающее дерево:")
for u, v, weight in minimum_spanning_tree:
    print(f"{u} -- {v}    Вес: {weight}")
