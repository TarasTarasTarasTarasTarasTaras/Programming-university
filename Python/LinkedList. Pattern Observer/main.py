from MyClassError import MyClassError
from LinkedList import LinkedList
from Validation import Validation
from Iterator import IteratorLL
from Generator import generator
from Strategy import *
from Observer import Observer
from Logger import Logger
from Event import Event
import random

validation = Validation()


def menu():
    while True:
        try:
            action = int(input("===============================================\n" + 
                               "1.  Choose a strategy 'Fill by Iterator'\n" + 
                               "2.  Choose a strategy 'Read from file'\n" + 
                               "3.  Generate data in a LinkedList\n" + 
                               "4.  Add the item by index\n" +
                               "5.  Add multiple items by index\n" +
                               "6.  Delete the item by index\n" + 
                               "7.  Delete items within the start and end positions\n" + 
                               "8.  Сyclically move the list by K positions\n" + 
                               "9.  Print LinkedList\n" + 
                               "0.  Exit\n" + 
                               "===============================================\n"))
            if action < 0 or action > 9:
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


def generate_data(linkedList, observer):
    old_list = linkedList.get_copy()

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
        added_elems = linkedList.execute_strategy(n, A, B, index)
        print("  <<< Data generated randomly successfully >>>")

    elif linkedList.get_strategy() == "read from file":
        filename = input("Enter file name in txt format: ")
        Validation.validate_format_file(filename)
        index = (0 if linkedList.get_size() == 0 else validation.validation_is_int(input("Enter the insert position:  ")))
        added_elems = linkedList.execute_strategy(filename, index)
        print("  <<< Data from the file was read successfully >>>")
        
    Event.update("add", observer, old_list, added_elems, index, linkedList.get_copy())


def add_an_item_by_index(linkedList, observer):
    old_list = linkedList.get_copy()
    item = input("Enter item: ")
    index = (0 if linkedList.get_size() == 0 else validation.validation_is_int(input("Enter the insert position:  ")))
    linkedList.insert(index, item)
    Event.update("add", observer, old_list, item, index, linkedList.get_copy())


def add_multiple_items_by_index(linkedList, observer):
    old_list = linkedList.get_copy()
    added_elems = []
    n = validation.validation_is_int(input("How many items do you want to add? "))
    index = (0 if linkedList.get_size() == 0 else validation.validation_is_int(input("Enter the insert position:  ")))
    for i in range(n):
        item = input("Enter item %i: " % (i+1))
        added_elems.append(item)
        linkedList.insert(index, item)
        index+=1

    Event.update("add", observer, old_list, added_elems, index-n, linkedList.get_copy())


def delete_the_item_by_index(linkedList, observer):
    old_list = linkedList.get_copy()
    index = input("Enter index: ")
    del_elem = linkedList.del_elem_by_index(index)
    Event.update("remove", observer, old_list, del_elem, index, linkedList.get_copy())


def delete_items_within_start_end(linkedList, observer):
    old_list = linkedList.get_copy()
    start = int(input("Enter the start index: "))
    end = int(input("Enter the end index: "))
    del_elems = linkedList.del_elem_from_start_to_end(start, end)
    Event.update("remove", observer, old_list, del_elems, [start, end], linkedList.get_copy())


def cyclically_move_by_K_positions(linkedList):
    K = input("How many items do you want to move the list to? ")
    linkedList.cyclic_shift_by_K_positions(K)


def print_linkedList(linkedList):
    print(linkedList)


def main():
    linkedList = LinkedList()
    logger = Logger("logs.txt")
    observer = Observer()
    observer.attach("add", logger.add_operation)
    observer.attach("remove", logger.remove_operation)
    

    dictionary_of_actions = {1 : choose_strategy_fill_by_iterator, 2 : choose_strategy_read_from_file, 3 : generate_data,
                             4 : add_an_item_by_index, 5: add_multiple_items_by_index, 6 : delete_the_item_by_index,
                             7 : delete_items_within_start_end, 8 : cyclically_move_by_K_positions, 9: print_linkedList}

    while True:
        print("Selected strategy: >>> " + linkedList.get_strategy() + "\n")
        action = menu()
        if action == 0: break
        else:
            try:
                if 2 < action < 8: dictionary_of_actions[action](linkedList, observer)
                else:              dictionary_of_actions[action](linkedList)
            except (MyClassError, ValueError, KeyError, FileNotFoundError) as message:
                print(str(message))




main()
