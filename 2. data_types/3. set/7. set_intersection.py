set_one = {"hp", "dell", "lenovo", "windows", "linux"}
set_two = {"sony", "mac", "windows", "linux"}

# set_two.intersection_update(set_one)    # It does not return value.
# print(set_two)
# print(set_one)

test_set = set_two.intersection(set_one)
print(set_two)
print(set_one)
print(test_set)
