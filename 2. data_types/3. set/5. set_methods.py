set_one = {"Dev", "QA", "Ops", 2021, "GitHub", "Java+Selenium"}
set_one.add("TEST")
print(set_one)

set_two = set_one.copy()
print(set_two)

set_one.clear()
print(set_one)

set_three = {"ADO", "Python+Selenium"}
set_four = {"ADO", "Python", "Java"}
difference = (set_three.difference(set_four))
print(difference)


