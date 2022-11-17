"""
    1. Constructor is an in build method created at run time while creating an object in class.
    2. Constructor is called automatically.
    3. __init__ is constructor name in Python unlike class name in another programming languages.

"""


class Test:

    def __init__(self):  # Constructor
        print("Constructor is called automatically.")

    def test_method(self):
        print("Welcome to Python OOP concepts.")


test_obj = Test()  # Object creation
test_obj.test_method()
