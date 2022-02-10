from MyClassError import MyClassError

class Validation:
    def validation_is_int(self, value):
        try:
            return int(value)
        except:
            raise MyClassError("  ERROR: Value must be INT\n")


    def index_validation_by_added(self, n:int, list_size:int):
        if n < 0 or n > list_size:
            raise MyClassError("  ERROR: Index must be '>' 0 and '<' " + str(list_size + 1) + " (list size)\n")


    def index_validation(self, n:int, list_size:int):
        if n < 0 or n >= list_size:
            raise MyClassError("  ERROR: Index must be '>' 0 and '<' " + str(list_size) + " (list size)\n")


    def number_validation_by_added(self, n:int):
        if n < 1 or n >= 100:
            raise MyClassError("  ERROR: Number of items must be '>' 0 and '<' 100\n")


    def validation_when_cyclic_shift(self, k:int, list_size:int):
        if k < 0 or k >= list_size:
            raise MyClassError("  ERROR: K must be '>' 0 and '<' " + str(list_size) + " (list size)\n")


    def validate_format_file(self, filename):
        if filename.endswith('.txt') is not True:
            raise ValueError("  ERROR: " + filename + " must be txt format")
