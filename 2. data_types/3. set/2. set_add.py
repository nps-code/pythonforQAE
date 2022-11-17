"""
    Like in list, we will not be able to use insert method to add items to a set as the method needs two parameters
    which are index and value. (Remember Set is Un-ordered and Un-Indexed). Hence, there is another method called
    add is available.
"""
set_three = {"Australia", "India", "Japan", "United States"}
print(set_three)
set_three.add("Israel")
print(set_three)
