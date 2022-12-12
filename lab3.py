x = int(input())
v=[]
a = 1
b=0
c=0
i=1
while a<=x:
    b=a
    while  b<=x:
        c=b
        while c<=x:
            v.append(c)
            i+=1
            c*=7
        b*=5
    a*=3

v.sort()
print(v)
