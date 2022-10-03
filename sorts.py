from random import randint


def combSort(list): # №4 Сортировка методом прочесывания
    n = len(list)
    factor = 1.3
    step = n
    while step > 1 or q:
        if step > 1:
            step = int(step // factor)
        q, i = False, 0
        while i + step < n:
            if list[i] > list[i + step]:
                list[i], list[i + step] = list[i + step], list[i]
                q = True
            i += step
    print(list)


def insertionSort(list): # №5 Вставками
    for i in range(len(list)):
        j = i - 1
        key = list[i]
        while list[j] > key and j >= 0:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    print(list)


def selectionSort(list): # №6 Посредством выбора
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[j]<list[i]:
                list[i],list[j]=list[j],list[i]
    print(list)


def shellSort(list): # №7 Шелла
    length = len(list)
    step = length//2
    while step>0:
        for i in range(step, length, 1):
            j = i
            k = j - step
            while k >= 0 and list[k] > list[j]:
                list[k],list[j]=list[j],list[k]
                j = k
                k = j - step
        step//=2
    print(list)


def radixSort(list): # №8 Поразрядная
    length = len(str(max(list)))
    rang = 10
    for i in range(length):
        ranks = [[] for j in range(rang)]
        for k in list:
            num = k // 10**i % 10
            ranks[num].append(k)
        list = []
        for j in range(rang):
            list = list + ranks[j]
    print(list)


def heapify(list, n, i): # №9 Пирамидальная (heap sort)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and list[i] < list[l]:
        largest = l
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)


def heapSort(list):
    n = len(list)
    for i in range(n // 2, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    print(list)


def mergeSort(A): # №10 Слиянием
    if len(A) == 1 or len(A) == 0:
        return A
    L = mergeSort(A[:len(A) // 2])
    R = mergeSort(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A


list = [randint(1, 100) for a in range(100)]
combSort(list)
list = [randint(1, 100) for a in range(100)]
insertionSort(list)
list = [randint(1, 100) for a in range(100)]
selectionSort(list)
list = [randint(1, 100) for a in range(100)]
shellSort(list)
list = [randint(1, 100) for a in range(100)]
radixSort(list)
list = [randint(1, 100) for a in range(100)]
heapSort(list)
list = [randint(1, 100) for a in range(100)]
mergeSort(list)
print(list)
