"""
    1.  We can add an item to existing list, using append method. It takes value as argument.
    2.  An item can be added to an existing list using insert method which has two arguments i.e. index and value.
    2.  It can be added at any place just by giving the required index.
    3.  * Though we give index which is greater than the length of the list, it is appended to the immediate next to the
        last item of the list.
    4.  The extra memory created as per the index will be erased.

"""
list_two = ["Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"]
print(list_two)
list_two.append("Scrum Team")
print(list_two)

list_two.insert(3, "Software")
print(list_two)

print(len(list_two))
list_two.insert(25, "Test Item")
print(list_two)
