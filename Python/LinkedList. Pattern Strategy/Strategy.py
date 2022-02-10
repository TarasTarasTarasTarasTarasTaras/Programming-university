from abc import abstractmethod
from Iterator import IteratorLL

class InterfaceStrategyFillList:
    @abstractmethod
    def execute(self, linkedList, *args):
        pass
    @abstractmethod
    def get_name(self):
        pass


class StrategyFillByIterator(InterfaceStrategyFillList):
    def execute(self, linkedList, n, A, B, index):
        func = IteratorLL(n, A, B)
        linkedList.fill_randomly(func, index)

    def get_name(self):
        return "fill by iterator"


class StrategyReadFromFile(InterfaceStrategyFillList):
    def execute(self, linkedList, filename, index):
        file = open(filename)
        items = file.readline()
        items = items.split(" ")
        for i in items:
            linkedList.insert(index, i)
            index+=1

    def get_name(self):
        return "read from file"
