class Calculator:
    constant_num = 1000  # Class variables defined at class level.

    def __init__(self, x, y):
        self.first_num = x  # first_num & second_num are instance variables defined at constructor.
        self.second_num = y
        print("Parent class constructor called automatically.")

    def total(self):
        return self.first_num + self.second_num
        # return self.first_num + self.second_num + self.constant_num
