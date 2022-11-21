from random import randint


def combSort(array): # №4 Сортировка методом прочесывания
    n = len(array)
    factor = 1.3
    step = n
    while step > 1 or q:
        if step > 1:
            step = int(step // factor)
        q, i = False, 0
        while i + step < n:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                q = True
            i += step
    print(array)


def insertionSort(array): # №5 Вставками
    for i in range(len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    print(array)


def selectionSort(array): # №6 Посредством выбора
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[j]<array[i]:
                array[i],array[j]=array[j],array[i]
    print(array)


def shellSort(array): # №7 Шелла
    length = len(array)
    step = length//2
    while step>0:
        for i in range(step, length, 1):
            j = i
            k = j - step
            while k >= 0 and array[k] > array[j]:
                array[k],array[j]=array[j],array[k]
                j = k
                k = j - step
        step//=2
    print(array)


def radixSort(array): # №8 Поразрядная
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        ranks = [[] for j in range(rang)]
        for k in array:
            num = k // 10**i % 10
            ranks[num].append(k)
        array = []
        for j in range(rang):
            array = array + ranks[j]
    print(array)


def heapify(array, n, i): # №9 Пирамидальная (heap sort)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    print(array)


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


def partition(array, start, end): # №11 Быстрая
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quickSort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)


array = [randint(1, 100) for a in range(100)]
combSort(array)
array = [randint(1, 100) for a in range(100)]
insertionSort(array)
array = [randint(1, 100) for a in range(100)]
selectionSort(array)
array = [randint(1, 100) for a in range(100)]
shellSort(array)
array = [randint(1, 100) for a in range(100)]
radixSort(array)
array = [randint(1, 100) for a in range(100)]
heapSort(array)
array = [randint(1, 100) for a in range(100)]
mergeSort(array)
print(array)
array = [randint(1, 100) for a in range(100)]
quickSort(array,0,len(array)-1)
print(array)
