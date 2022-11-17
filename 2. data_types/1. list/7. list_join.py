""" We have different ways to join or concatenate, two or more lists in Python.
    1. using + operator
    2. using extend
    3. appending items using iteration
"""

list_one = ["Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"]
list_two = ["ADO", "Python+Selenium"]
list_three = list_one + list_two     # using + operator
print(list_three)

list_four = ["U.S.", "ASIA", "EMEA"]
list_five = ["America", "India", "Dubai"]
list_six = list_four.extend(list_five)
print(list_six)  # Prints None as extend and assignment does not work if done in the same line.
print(list_four.extend(list_five))  # Prints None as extend and assignment does not work if done in the same line.
print(list_four)  # Right approach.

list_seven = ['a', 'b', 'c', 'd']
list_eight = [1, 2, 3, 4]
for item in list_seven:      # using + operator
    list_eight.append(item)
print(list_eight)
