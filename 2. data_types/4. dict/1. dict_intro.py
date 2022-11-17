"""
    1. Dictionaries can have values of same or different data types.
    2. Values are stored in the dictionary in the form of key, value pair.
    3. They are ordered.
    4. The values are accessible by using key.
    5. The dictionary items are changeable.
    6. Duplicate items are not allowed means Dictionary can't have two items with the same key.
        The latest value assigned to the key is always over writes the previous value.
"""
dict_one = {
    "name": "charan",
    "class": 6,
    "roll_no": 12345,
    "value": True,
    "value": False
    }
# Point 1, 2, 3, 4
print(dict_one)
print(dict_one["name"])

# Point 5
dict_one["name"] = "cp"
dict_one["school"] = "SIS"
print(dict_one["school"])

# Point 6
print(dict_one["value"])

# To find length of a dictionary.
print(len(dict_one))
