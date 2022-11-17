"""
   1. To know the keys & values of a dictionary.
   2. Extracting required data from a dictionary
   3. Changing values of a dictionary.
"""
dict_two = {
    "country": "India",
    "code": 91,
    "metros": ["Delhi", "Chennai", "Mumbai", "Kolkata"],
    "capital": "Delhi"
}
print(dict_two.keys())  # To know all of the keys in a given dictionary.
print(dict_two.values())  # To know all of the items in a given dictionary.
print(dict_two.items())  # It returns each item in a dictionary, as tuples in a list.
test_list = dict_two.items()
# print(test_list[2])  # It throws an error though items method returns values in a list.

print(dict_two["code"])  # To find the value assigned to 'code' key.
print(dict_two.get("code"))  # get() method can be also used to get value of a given key.

dict_two["capital"] = "New Delhi"  # Changing the value.
print(dict_two)

# To check if a given Key exists in the dictionary.
if "code" in dict_two:
    print("It exists")
