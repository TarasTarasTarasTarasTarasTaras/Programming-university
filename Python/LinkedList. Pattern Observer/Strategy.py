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
        added_elems = linkedList.fill_randomly(func, index)
        return added_elems

    def get_name(self):
        return "fill by iterator"


class StrategyReadFromFile(InterfaceStrategyFillList):
    def execute(self, linkedList, filename, index):
        file = open(filename)
        items = file.readline()
        items = items.split(" ")
        added_elems = []
        for i in items:
            added_elems.append(i)
            linkedList.insert(index, i)
            index+=1
        return added_elems

    def get_name(self):
        return "read from file"
