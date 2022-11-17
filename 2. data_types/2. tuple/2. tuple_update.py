"""
    Once a tuple is created, we cannot change its values. Tuples are unchangeable or immutable as it also is called.
But we can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
tuple_two = ("QA", "QA", "Ops", 2021, "GitHub", "Java+Selenium")
list_two = list(tuple_two)
print("after converting tuple to list: ", list_two)

list_two.append("List/Tuple conversion")
print("after appending a value", list_two)

tuple_two = tuple(list_two)
print(tuple_two)

del tuple_two
# print("after deleting tuple: ", tuple_two)


