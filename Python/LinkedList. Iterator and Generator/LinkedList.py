import random
from Node import Node
from Validation import Validation
from MyClassError import MyClassError


class LinkedList:
    def __init__ (self):
        self.__head = None
        self.__last = None
        self.__int_size = 0
        self.__validation = Validation()


    def enter_from_the_keyboard(self, n:int):
        try:
            n = self.__validation.validation_is_int(n)
            self.__validation.number_validation_by_added(n)
        except MyClassError as message:
            print(str(message))
            return False

        for i in range(n):
            value = input("LinkedList [" + str(self.__int_size) + "] = ")
            self.append(value)


    def fill_randomly(self, func):
        for value in func:
            self.append(value)


    def append(self, value):
        new_elem = Node(value)
        if self.__head is None and self.__last is None:
            self.__head = self.__last = new_elem
        else:
            new_elem.prev = self.__last
            self.__last.next = new_elem
            self.__last = new_elem
        self.__int_size+=1


    def insert(self, index:int, value):
        try:
            index = self.__validation.validation_is_int(index)
            self.__validation.index_validation_by_added(index, self.__int_size)
        except MyClassError as message:
            print(message)
            return False

        if index == 0:
            new_elem = Node(value, self.__head, None)
            self.__head.prev = new_elem
            self.__head = new_elem

        elif index == self.__int_size:
            new_elem = Node(value, None, self.__last)
            self.__last.next = new_elem
            self.__last = new_elem

        else:
            if index < self.__int_size//2:
                сurr_index = 0
                curr_elem = self.__head
                while(curr_index != index):
                    curr_index += 1
                    curr_elem = curr_elem.next
            else:
                curr_index = self.__int_size - 1
                curr_elem = self.__last
                while(curr_index != index):
                    curr_index -= 1
                    curr_elem = curr_elem.prev

            new_elem = Node(value, curr_elem, curr_elem.prev)
            curr_elem.prev.next = new_elem
            new_elem.next.prev = new_elem
        self.__int_size += 1


    def pop(self):
        try:
            self.__validation.index_validation(self.__int_size - 1)
        except MyClassError as message:
            print(message)
            return False
        returned_value = self.__last
        self.__last = self.__last.prev
        __int_size -= 1
        return returned_value


    def del_elem_by_index(self, index:int):
        try:
            index = self.__validation.validation_is_int(index)
            self.__validation.index_validation(index, self.__int_size)
        except MyClassError as message:
            print(message)
            return False

        if index == 0:
            self.__head = self.__head.next
            self.__head.prev = None

        elif index == self.__int_size - 1:
            self.__last = self.__last.prev
            self.__last.next = None

        else:
            if index < self.__int_size//2:
                curr_index = 0
                curr_elem = self.__head
                while(curr_index != index):
                    curr_index += 1
                    curr_elem = curr_elem.next
            else:
                curr_index = self.__int_size - 1
                curr_elem = self.__last
                while(curr_index != index):
                    curr_index -= 1
                    curr_elem = curr_elem.prev
            
            curr_elem.prev.next = curr_elem.next
            curr_elem.next.prev = curr_elem.prev
        self.__int_size -= 1


    def cyclic_shift_by_K_positions(self, k:int):
        try:
            k = self.__validation.validation_is_int(k)
            self.__validation.validation_when_cyclic_shift(k, self.__int_size)
        except MyClassError as message:
            print(message)
            return False

        if k < self.__int_size//2:
            curr_index = 0
            curr_elem = self.__head
            while(curr_index != k):
                curr_index += 1
                curr_elem = curr_elem.next
        else:
            curr_index = self.__int_size - 1
            curr_elem = self.__last
            while(curr_index != k):
                curr_index -= 1
                curr_elem = curr_elem.prev

        self.__last.next = self.__head
        self.__head.prev = self.__last
        self.__head = curr_elem
        self.__last = curr_elem.prev
        self.__head.prev = None
        self.__last.next = None


    def get_first_elem(self):
        return self.__head.value


    def get_last_elem(self):
        return self.__last.value


    def get_elem_by_index(self, index:int):
        try:
            index = self.__validation.validation_is_int(index)
            self.__validation.index_validation(index, self.__int_size)
        except MyClassError as message:
            print(message)
            return False

        if index < self.__int_size//2:
            curr_index = 0
            curr_elem = self.__head
            while(curr_index != index):
                curr_index += 1
                curr_elem = curr_elem.next
        else:
            curr_index = self.__int_size - 1
            curr_elem = self.__last
            while(curr_index != index):
                curr_index -= 1
                curr_elem = curr_elem.prev
        return curr_elem.value


    def get_size(self) -> int:
        return self.__int_size


    def __print_list(self) -> str:
        curr_elem = self.__head
        string = "[ "
        while(curr_elem is not None):
            string += str(curr_elem.value) + " "
            curr_elem = curr_elem.next
        string += "]"
        return string

    
    def __str__(self):
        return self.__print_list()


    def __repr__(self):
        return self.__print_list()


    def __getitem__(self, index):
        return self.get_elem_by_index(index)


    def __len__(self):
        return self.__int_size


    def __setitem__(self, index, value):
        try:
            self.__validation.validation_is_int(index)
            self.__validation.index_validation(index, self.__int_size)
        except MyClassError as message:
            print(message)
            return False

        if index < self.__int_size//2:
            curr_index = 0
            curr_elem = self.__head
            while(curr_index != index):
                curr_index += 1
                curr_elem = curr_elem.next
        else:
            curr_index = self.__int_size - 1
            curr_elem = self.__last
            while(curr_index != index):
                curr_index -= 1
                curr_elem = curr_elem.prev
        curr_elem.value = value
