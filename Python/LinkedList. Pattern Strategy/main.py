from MyClassError import MyClassError
from LinkedList import LinkedList
from Validation import Validation
from Iterator import IteratorLL
from Generator import generator
from Strategy import *
import random

validation = Validation()


def menu():
    while True:
        try:
            action = int(input("===============================================\n" + 
                               "1.  Choose a strategy 'Fill by Iterator'\n" + 
                               "2.  Choose a strategy 'Read from file'\n" + 
                               "3.  Generate data in a LinkedList\n" + 
                               "4.  Delete the item by index\n" + 
                               "5.  Delete items within the start and end positions\n" + 
                               "6.  Сyclically move the list by K positions\n" + 
                               "7.  Print LinkedList\n" + 
                               "8.  Exit\n" + 
                               "===============================================\n"))
            if action < 1 or action > 8:
                print("Please try again")
            else: return action
        except ValueError:
            print("Must be INT")
            continue
    
        
def choose_strategy_fill_by_iterator(linkedList):
    linkedList.set_strategy(StrategyFillByIterator())
    print("Strategy 'Fill by Iterator' selected successfully")


def choose_strategy_read_from_file(linkedList):
    linkedList.set_strategy(StrategyReadFromFile())
    print("Strategy 'Read from file' selected successfully")


def generate_data(linkedList):
    if linkedList.get_strategy() == "fill by iterator":
        n = validation.validation_is_int(input("How many items do you want to add? "))
        validation.number_validation_by_added(n)
        A = validation.validation_is_int(input("Enter A: "))
        B = validation.validation_is_int(input("Enter B: "))
        index = (0 if linkedList.get_size() == 0 else validation.validation_is_int(input("Enter the insert position:  ")))
        if A > B:
            A=A+B
            B=A-B
            A=A-B
        linkedList.execute_strategy(n, A, B, index)
        print("  <<< Data generated randomly successfully >>>")
    elif linkedList.get_strategy() == "read from file":
        filename = input("Enter file name in txt format: ")
        validation.validate_format_file(filename)
        index = (0 if linkedList.get_size() == 0 else validation.validation_is_int(input("Enter the insert position:  ")))
        linkedList.execute_strategy(filename, index)
        print("  <<< Data from the file was read successfully >>>")
        

def delete_the_item_by_index(linkedList):
    index = input("Enter index: ")
    linkedList.del_elem_by_index(index)


def delete_items_within_start_end(linkedList):
    start = int(input("Enter the start index: "))
    end = int(input("Enter the end index: "))
    linkedList.del_elem_from_start_to_end(start, end)


def cyclically_move_by_K_positions(linkedList):
    K = input("How many items do you want to move the list to? ")
    linkedList.cyclic_shift_by_K_positions(K)


def print_linkedList(linkedList):
    print(linkedList)


def main():
    linkedList = LinkedList()
    
    dictionary_of_actions = {1 : choose_strategy_fill_by_iterator, 2 : choose_strategy_read_from_file,
                             3 : generate_data, 4 : delete_the_item_by_index, 5 : delete_items_within_start_end,
                             6 : cyclically_move_by_K_positions, 7: print_linkedList}

    while True:
        print("Selected strategy: >>> " + linkedList.get_strategy() + "\n")
        action = menu()
        if action == 8: break
        else:
            try:
                dictionary_of_actions[action](linkedList)
            except (MyClassError, ValueError, KeyError, FileNotFoundError) as message:
                print(str(message))




main()
