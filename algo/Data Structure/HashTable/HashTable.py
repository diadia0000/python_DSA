import math


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        parseKey = 0
        if type(key) != int:
            parseKey = self.parse(key)
        else:
            parseKey = key
        A = (math.sqrt(5) - 1) / 2
        return math.floor(self.size * ((parseKey * A) % 1))

    def set(self, key, value):
        index = self.hash2(key)
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash2(key)  # Use the same hash function in set
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Return the value part of the key-value
        return None

    # parse string to integer
    def parse(self, Str):
        result = 0
        for i in range(0, len(Str)):
            result += ord(Str[i])
        return result % self.size

    def printTable(self):
        print(self.table)


Map = HashTable(6)

Map.set("white","#FFFFFF")
Map.set("magenta", "#FF00FF")
Map.set("red", "#FF0000")

Map.printTable()
print(Map.get("red"))