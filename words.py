letters=list('комбинаторика')
n=len(letters)
words=set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            for m in range(n):
                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                    words.add(letters[i]+letters[j]+letters[k]+letters[m])
print(len(words))
