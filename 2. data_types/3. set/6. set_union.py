set_one = {"Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"}
set_two = {"ADO", "Python+Selenium"}

# set_three = set_one + set_two
# print(set_three)  # Concatenation of sets is not supported.

set_three = set_one.union(set_two)
print(set_three)
