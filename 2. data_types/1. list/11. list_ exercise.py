list_one = ["DevOps", "DevOps", "DevOps", 2021, 2021, 2021, 2021]

list_one.append("QA")
print(list_one)
print(list_one.count(2021))
print(list_one.count("DevOps"))

list_two = ["Hundai", "Skoda", "Audi", "Benz", "Maruthi", "Honda"]
list_two.sort()
print(list_two)

list_three = []
list_three = list_two.copy()
print(list_three)

list_two.clear()
print(list_two)

list_four = ["HP", "DELL", "LENOVO", "ACER"]
list_four.insert(0, "Laptop")
print(list_four)

list_four.pop()
print(list_four)

list_four.remove("HP")
print(list_four)

list_four.extend(list_one)
print(list_four)
print(list_four[4])


