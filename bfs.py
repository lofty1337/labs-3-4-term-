A = [
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]   #матрица смежности

d = [-1] * len(A)

def bfs(s):
    global d
    d[s] = 0
    q = [s]
    while q:
        v = q.pop(0)
        for u in A[v]:
            if d[u] == -1:#проверка на посещенность
                q.append(u)
                d[u] = d[v] + 1

bfs(0)
print(d)
