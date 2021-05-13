import collections
from collections import defaultdict

class BooleanFunction:
    def __init__(self):
        self.__map = defaultdict()
        self.functionClass = 0
        self.functionCategories = []

    def getFunction(self):
        return list(self.__map.values())

    def addValue(self, input, output):
        self.__map[input] = output

    def getFunctionClass(self):
        return self.functionClass

    def getFunctionCategories(self):
        return self.functionCategories

    def setClass(self, fClass):
        self.functionClass = fClass

    def getValue(self, input):
        return self.__map[input]

    def __str__(self):
        sMap = sorted(list(self.__map.items()))
        out = str(self.functionClass) + ";"
        for keys in sMap:
            out += str(keys[1])

        return out

    def __lt__(self, other):
        return self.functionClass < other.functionClass

    def __hash__(self):
        return hash(frozenset(self.__map.items()))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return collections.Counter(self.__map) == collections.Counter(other.__map)
