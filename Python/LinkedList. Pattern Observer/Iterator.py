import random

class IteratorLL:
    def __init__(self, size, *args, function = random.randint):
        self.__args = args
        self.__curr_index = 0
        self.__size = size
        self.__function = function
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curr_index >= self.__size:
            raise StopIteration
        self.__curr_index += 1
        return self.__function(*self.__args)



