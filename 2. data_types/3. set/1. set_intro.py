""" 1. Sets are used to store multiple values of same or different types like String, Number, Boolean
        in a single variable.
    2. It is represented by {}
    3. Set is Un-ordered & Un-Indexed
    4. Duplicate values are not allowed. (at the time of declaring a set we can add duplicate items but
        they are deleted at run time.
"""

set_one = {"Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False}
print(set_one)   # Point 1, 2 & 3 run it multiple times to observe how they are un-ordered.


set_two = {"Python", "Python", "Python", "Python", True, 1, 0, False}
print(set_two)  # Point 4, observe the O/P and remember True returns value 1 and False returns 0 value.

print("Python" in set_two)  # Just to validate a given item in the set.
print(len(set_one))     # To find length of a set.
