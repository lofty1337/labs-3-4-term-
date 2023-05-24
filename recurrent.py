def recurrent(k):
    if k==0:
        return 5
    if k==1:
        return 6
    else:
        return int(7*recurrent(k-1)-12*recurrent(k-2))
def general(k):
    return int(14*3**k-9*4**k)
n=10
print(recurrent(n))
print()
print(general(n))
