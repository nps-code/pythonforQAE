"""
    1. If any constructor defined in parent class, then we need to create the same in child class too.
    2. We can access the parent constructor with the help of parent class name (line 13)
"""

from parent_class import Calculator


class Test(Calculator):
    child_num = 500

    def __init__(self):
        Calculator.__init__(self, 20, 30)

    def get_data(self):
        return self.first_num + self.second_num + self.total() + self.child_num


test_obj = Test()
print(test_obj.get_data())

