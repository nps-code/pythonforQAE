""" 1. Tuples are used to store multiple items of different types like String, Number, Boolean in a single variable.
    2. It is represented by ()
    3. Tuple items are ordered, un-changeable, allow duplicate values and can be accessed by index.
    4. Usage of -ve index is allowed in Tuple.
    5. Index of a Tuple starts from 0.
"""

tuple_one = ("Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False)

print("tuple items: ", tuple_one)
print("accessing data by index 3: ", tuple_one[3])
print("accessing data by specific index range 4 to 6: ", tuple_one[4:6])
print("accessing data up to the upper index specified 5: ", tuple_one[:5])  # starts from 0 and ends at 5-1.
print("from given index to last item: ", tuple_one[2:])  # item count starts from 2.
print("accessing data using -ve index -1: ", tuple_one[-1])  # first item in reverse order.
print("from index 2 to -3: ", tuple_one[2:-3])  # starts from 2 in forward direction and ends at -3-1=-4 from
# backward direction.
print("length of the list", len(tuple_one))
print("from index 4 to 20 which is out of range: ", tuple_one[4:20])  # starts from 4 and ends at last item as the
# upper index is greater than length of the list.
print("from index 20 which is out of range: ", tuple_one[20:])  # prints empty tuple as there is no item placed at the
# index which is greater than length of the list.
print("to index 20 which is out of range: ", tuple_one[:20])  # prints complete tuple as the upper index given
# is greater than the length of the list.
print("from 20 to 25 index which is out of range: ", tuple_one[20:25])  # prints empty tuple as there is no items placed
# in the range which greater than length of the list.
print("list with -ve index range: ", tuple_one[-5:-3])
print("list with -ve index invalid range: ", tuple_one[-5:-6])  # prints empty tuple as the order is invalid.
print(tuple_one[9])  # IndexError: list index out of range as len is 8
