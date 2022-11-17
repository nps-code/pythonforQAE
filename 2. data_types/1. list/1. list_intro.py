"""
    1. List can store values of same or different data types.
    2. List is represented by []
    3. Items are stored in a list using index.
    3. Items in the list are ordered.
    4. The items are accessible by using index.
    5. The list of items are changeable.
    6. Duplicate items are allowed in a list.

 """

list_one = ["Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False, 22]
print("list items: ", list_one)
print("accessing data by index 3: ", list_one[3])  # index starts from 0.
print("accessing data by specific index range 4 to 6: ", list_one[4:6])  # starts from 4 and ends at 6-1 always.
print("accessing data up to the upper index specified 5: ", list_one[:5])  # starts from 0 and ends at 5-1.
print("from given index to last item: ", list_one[2:])  # item count starts from 2.
print("accessing data using -ve index -1: ", list_one[-1])  # first item in reverse order.
print("from index 2 to -3: ", list_one[2:-3])  # starts from 2 in forward direction and ends at -3-1=-4 from
# backward direction.
print("length of the list", len(list_one))
print("from index 4 to 20 which is out of range: ", list_one[4:20])  # starts from 4 and ends at last item as the
# upper index is greater than length of the list.
print("from index 20 which is out of range: ", list_one[20:])  # prints empty list as there is no item placed at the
# index which is greater than length of the list.
print("to index 20 which is out of range: ", list_one[:20])  # prints complete list as the upper index given is greater
# than the length of the list.
print("from 20 to 25 index which is out of range: ", list_one[20:25])  # prints empty list as there is no items placed
# in the range which greater than length of the list.
print("list with -ve index range: ", list_one[-5:-3])
print("list with -ve index invalid range: ", list_one[-5:-6])  # prints empty list as the order is invalid.
print(list_one[1:8:3])  # It prints from index 1 to 8 skipping 2(3-1) items in between.
# # print(list_one[9])  # IndexError: list index out of range as len is 8

 