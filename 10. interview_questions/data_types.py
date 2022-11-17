list_one = ["Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False]

#   1.What is the out put of
print("from 20 to 25 index which is out of range: ", list_one[20:25])  # prints empty list as there is no items placed
# in the range which greater than length of the list.
print("list with -ve index range: ", list_one[-5:-3])
print("list with -ve index invalid range: ", list_one[-5:-6])  # prints empty list as the order is invalid.

#   2.How to access the newly added item to the list and what is the length of the list.
list_one.insert(20, "TEST")
print(list_one)
print(len(list_one))

list_two = ["Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"]

#   3.How do you replace items in a given list for a selected range.
list_two[4:6] = ["ADO", "Python+Selenium"]
print(list_two)

list_three = ["U.S.", "ASIA", "EMEA"]
#   4. How do you append a list of items to another list? and what happens if we assign it to a variable?
list_two.extend(list_three)
print(list_two)

tes_list = list_two.extend(list_three)

print(tes_list)

#   5.Difference among append, insert and extend methods of a list?

#   6.Difference among remove, pop, del and clear methods of a list?

#   7. How to sort the items of a list by disabling case sensitive?

#   8. Is there a way to change items of Tuple?

#   9. What are the methods of Tuple that return values?

set_one = {"Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False}
#   10. Difference between set_one.remove("TEST") & set_one.discard("TEST")
set_one.remove("TEST")
set_one.discard("TEST")
