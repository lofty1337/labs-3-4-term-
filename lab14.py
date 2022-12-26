# Хеш-таблица со списками
class HashTable:
    def __init__(self, size=10):
        self.capacity = self.getPrime(size)  # размер хеш-таблицы
        self.table = [[] for i in range(self.capacity)]
        self.keys = []  # список ключей

    def checkPrime(self, n):
        if (n == 1 or n == 0):
            return 0
        for i in range(2, n // 2):
            if n % i == 0:
                return 0
        return 1

    def getPrime(self, n):
        if n % 2 == 0:
            n += 1
        while not self.checkPrime(n):
            n += 1
        return n

    def hashFunction(self, key):
        return key % self.capacity


    def insertItem(self, key, data):
        i = self.hashFunction(key)
        if (i not in self.keys):
            self.keys.append(i)
        self.table[i].append(data)


    def searchItem(self, data):
        res = 0
        keyVal = 0
        for i in data:
            keyVal += ord(i)
        key = self.hashFunction(keyVal)
        for j in self.table[key]:
            if j == data:
                res += 1
        return res

    def printTable(self):
        for key in self.keys:
            print(f'{key} ', end='')
            for obj in self.table[key]:
                print(obj, end=' ')
            print()


table = HashTable(100)
s = input().split()

keyVal = 0
for word in s:
    for symbol in word:
        keyVal += ord(symbol)
    table.insertItem(keyVal, word)
    keyVal = 0

print(table.searchItem('zxc'))
table.printTable()
