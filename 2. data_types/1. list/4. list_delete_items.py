list_five = ["Hundai", "Skoda", "Audi", "Benz", "Maruthi", "Honda"]
print(list_five)
list_five.remove("Hundai")
print(list_five)

list_five.pop()  # By default, it removes the last item.
print(list_five)

list_five.pop(1)  # It removes the item by specified index and returns the removed value.
print(list_five)

x = list_five.pop(1)
print(x)

del list_five[1]
print(list_five)  # It removes the item by specified index but does not return any value.

list_six = [1, 2, 3, 'A', 'B', 'C']
print(list_six)
list_six.clear()
print(list_six)

# del list_six["A"]   # TypeError: list indices must be integers or slices, not str
del list_six
# print(list_six)
