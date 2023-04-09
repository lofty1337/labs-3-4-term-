backPackW=int(input("Вместимость рюкзака: "))
n=int(input("Количество предметов: "))
w=[]
p=[]
count=0
while count<n:
    i=input("Вес предмета: ")
    j=input("Ценность предмета: ")
    if i == 'q':
        break
    else:
        w.append(int(i))  #W=14 n=4 5,3 10,5 6,4 5,2
        p.append(int(j))  #W=4 n=3 4,3000 3,2000 1,1500
    count+=1
print(w)
print(p)
c=[[0] * backPackW for i in range(n)]
for i in range(1,n):
    for j in range(backPackW):
        c[i][j]=max(c[i-1][j],p[i]+c[i-1][j-w[i]])
print(c[n-1][backPackW-1])
