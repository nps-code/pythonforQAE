list_two = ["Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"]
print(list_two)
print(list_two.index("Ops"))  # To find index of required item.
list_two[2] = "DevOps"  # To replace an item with the new item using index.
print(list_two)

list_two[4:6] = ["ADO", "Python+Selenium"]  # Replacing multiple values by index range.
print(list_two)
