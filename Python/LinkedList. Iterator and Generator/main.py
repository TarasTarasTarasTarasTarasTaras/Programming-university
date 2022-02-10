from MyClassError import MyClassError
from LinkedList import LinkedList
from Validation import Validation
from Iterator import IteratorLL
from Generator import generator
import random

validation = Validation()


def menu():
    while True:
        try:
            action = int(input("===============================================\n" +
                               "1.  Print LinkedList\n" +
                               "2.  Enter items from the keyboard\n" +
                               "3.  Add random elements in the interval [A-B]\n" + 
                               "4.  Add an item by index\n" +
                               "5.  Delete the item by index\n" +
                               "6.  Сyclically move the list by K positions\n" + 
                               "7.  Exit\n" + 
                               "===============================================\n"))
            if action < 1 or action > 7:
                print("Please try again")
            else: return action
        except ValueError:
            print("Must be INT")
            continue
    
        
def print_linkedList(linkedList):
    print(linkedList)


def enter_items_from_keyboard(linkedList):
    n = input("How many items do you want to add? ")
    linkedList.enter_from_the_keyboard(n)


def add_random_elements(linkedList):
    while True:
        action = input("---------------------------------------\n"
                       "   1. Add random values using the Iterator\n" +
                       "   2. Add random values using the Generator\n" + 
                       "   3. Go back\n" + 
                       "---------------------------------------\n") 
        if action == "3": return
        elif action != "1" and action != "2":
            print("Please try again")
            continue
        else:
            n = validation.validation_is_int(input("How many items do you want to add? "))
            A = validation.validation_is_int(input("Enter A: "))
            B = validation.validation_is_int(input("Enter B: "))
            if A > B:
                    A=A+B
                    B=A-B
                    A=A-B
            if action == "1": func = IteratorLL(n, A, B)
            else:             func = generator(n, A, B)

            linkedList.fill_randomly(func)



def add_an_item_by_index(linkedList):
    item = input("Enter item: ")
    index = input("Enter index: ")
    linkedList.insert(index, item)


def delete_the_item_by_index(linkedList):
    index = input("Enter index: ")
    linkedList.del_elem_by_index(index)


def cyclically_move_by_K_positions(linkedList):
    K = input("How many items do you want to move the list to? ")
    linkedList.cyclic_shift_by_K_positions(K)


def main():
    linkedList = LinkedList()
    
    dictionary_of_actions = {1 : print_linkedList, 2 : enter_items_from_keyboard, 3 : add_random_elements,
                             4 : add_an_item_by_index, 5 : delete_the_item_by_index, 6 : cyclically_move_by_K_positions}

    while True:
        action = menu()
        if action == 7: break
        else:
            try:
                dictionary_of_actions[action](linkedList)
            except (MyClassError, ValueError, KeyError) as message:
                print(str(message))




main()
