dict_one = {
    "name": "charan",
    "class": 6,
    "roll_no": 12345,
    "value": True,
    "value": False
    }
# dict_one.popitem()  # last key is popped out
pop_ele = dict_one.pop("name")  # it returns the value of popped item.
print(pop_ele)
# del dict_one["class"]  # it does not return the value of deleted item.
# dict_one.clear()
# del dict_one
print(str(dict_one))
