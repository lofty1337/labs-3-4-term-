points = []

while True:
    point=[]
    x = input('x: ')
    y = input('y: ')
    if x == 'q' or y == 'q':
        break
    else:
        point.append(float(x))
        point.append(float(y))
        points.append(point)
print(points)

n = len(points)
A = list(range(n))

for i in range(1,n):
    if points[A[i]][0]<points[A[0]][0]:
        A[i],A[0] = A[0],A[i] # Ищем самую левую точку

B = [A[0]]#B будет хранить МВО
del A[0]
A.append(B[0])#самая левая точка гарантированно лежит в МВО

while True:
    right = 0
    for i in range(1, len(A)):
        p1=points[B[-1]]#ищем самую правую точку из A относительно последней вершины в B
        p2=points[A[right]]
        p3=points[A[i]]
        side=(p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
        if side < 0:
            right = i
    if A[right] == B[0]:#Если эта вершина стартовая, то прерываем цикл
        break
    else:#иначе переносим найденную вершину из A в B
        B.append(A[right])
        del A[right]

print("МВО:")
for i in range(len(B)):#в B находится искомая оболочка
    print(points[B[i]])
