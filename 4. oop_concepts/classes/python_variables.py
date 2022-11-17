"""
    1. There are two types of variables class variables and instance variables.
    2. We must use 'self' key word inside any method created everytime.
    3. 'self' keyword is mandatory while calling any variables.
    4. While passing parameters at class level, we need catch them at constructor.
    5. When we create an object to connect to a class, that objet is passed as self.

"""


class Calculator:
    constant_num = 1000  # Class variables defined at class level.

    def __init__(self, x, y):
        self.first_num = x  # first_num & second_num are instance variables defined at constructor.
        self.second_num = y

    def total(self):
        # return self.first_num + self.second_num
        return self.first_num + self.second_num + self.constant_num


test_obj = Calculator(10, 15)  # Providing arguments to the Class.
print(test_obj.total())

test_obj = Calculator(11, 12)  # Providing arguments to the Class.
print(test_obj.total())
