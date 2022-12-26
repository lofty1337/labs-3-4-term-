# Хеш-таблица с наложением
class HashTable():
    def __init__(self, size=10):
        self.A = 0.618033  # Золотое сечение – такое деление величины на две части,
        self.N = 13        # при котором отношение большей части к меньшей равно отношению всей величины к ее большей части.
        self.capacity = self.getPrime(size)  # размер хеш-таблицы
        self.table = {key: None for key in range(self.capacity)}
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

    def hashFunctionMod(self, key):
        return key % self.capacity

    def hashFunctionComb(self, key):
        return self.N * ((key * self.A) % 1)

    def hashFunctionPowered(self, key):
        return (self.hashFunctionMod(key) + self.hashFunctionComb(key)) // 1


    def insertItem(self, key, data):
        index = self.hashFunctionPowered(key)
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

    def printHash(self):
        for key in self.keys:
            print(f'{key} {self.table[key]}')


    def searchItem(self, data):
        key_val = 0
        for i in data:
            key_val += ord(i)

        index = self.hashFunctionPowered(key_val)
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
table.printHash()
