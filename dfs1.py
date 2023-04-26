def dfs(v, d, A, components, component_num):
    d.add(v)
    components[component_num].append(v)
    for next_vertex in A[v] - d:
        dfs(next_vertex, d, A, components, component_num)

def find_components(A):
    d = set()
    components = {}
    component_num = 1
    for v in A:
        if v not in d:
            components[component_num] = []
            dfs(v, d, A, components, component_num)
            component_num += 1
    return components

# Пример использования
A = {0: {1, 2}, 1: {0}, 2: {0}, 3: {4}, 4: {3}}
components = find_components(A)

for component_num, vertices in components.items():
    print(f'Компонента связности {component_num}: {vertices}')
