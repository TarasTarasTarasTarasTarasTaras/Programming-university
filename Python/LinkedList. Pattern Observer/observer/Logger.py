from Validation import Validation
from datetime import *

class Logger:
    def __init__(self, filename):
        self.__filename = filename

    def add_operation(self, old_list, list_of_values, pos, new_list, filename = "not specified"):
        if filename == "not specified": filename = self.__filename
        try:
            Validation.validate_format_file(filename)
            file = open(filename, mode="a")
        except FileNotFoundError:
            raise ValueError("File logger not found")
        
        file.write("------------Add operation------------\n" +
                   "Date:             " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n' +
                   "Old list:         " + str(old_list) + '\n' +
                   "Added items:      " + str(list_of_values) + '\n' +
                   "Position/Range:   " + str(pos) + '\n' +
                   "New list(result): " + str(new_list) + '\n' +
                   "-------------------------------------\n\n")


    def remove_operation(self, old_list, list_of_values, pos_or_range, new_list, filename = "not specified"):
        if filename == "not specified": filename = self.__filename
        try:
            Validation.validate_format_file(filename)
            file = open(filename, mode="a")
        except FileNotFoundError:
            raise ValueError("File logger not found")
        
        file.write("-----------Delete operation-----------\n" +
                   "Date:             " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n' +
                   "Old list:         " + str(old_list) + '\n' +
                   "Deleted items:    " + str(list_of_values) + '\n' +
                   "Position/Range:   " + str(pos_or_range) + '\n' +
                   "New list(result): " + str(new_list) + '\n' +
                   "--------------------------------------\n\n")

