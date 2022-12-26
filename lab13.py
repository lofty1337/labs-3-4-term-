# Хеш-таблица с наложением
class HashTable():
    def __init__(self, size=10):

        self.capacity = self.getPrime(size)
        self.table = {key: None for key in range(self.capacity)}
        self.keys = []

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
        index = self.hashFunction(key)
        if (not self.table[index]):
            self.keys.append(index)
        else:
            i = 0
            while True:
                if (not self.table[index + i]):
                    index += i
                    self.keys.append(index)
                    break
                i += 1
        self.table[index] = data

    def printTable(self):
        for key in self.keys:
            print(f'{key} {self.table[key]}')


    def searchItem(self, data):
        key_val = 0
        for i in data:
            key_val += ord(i)

        index = self.hashFunction(key_val)
        count, i = 0, 0
        while True:
            if (not (self.table[index + i])):
                break
            if (self.table[index + i] == data):
                count += 1
            i += 1
        return count


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
