list_two = ["Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"]

list_two.insert(0, "Test Item")
print("adding an item by using index: ", list_two)

list_two.append("Scrum Team")
print("after appending ", list_two)

list_three = ["U.S.", "ASIA", "EMEA"]
list_four = (list_two.extend(list_three))
print(list_four)  # prints empty list as extend and assignment do not work if done in the same line.?
print(list_two)
list_four = list_two
print(list_four)
