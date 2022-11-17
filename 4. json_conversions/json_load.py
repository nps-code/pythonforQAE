"""
    1. 'json.load' is method used to read the data of a json file.
"""
import json
with open(r"D:\np\test_files\user_details.json", "r") as file:
    data = json.load(file)

print(type(data))   # It returns the data in the form of dictionary.
print(data)

#  To read the required values only.
user_details = data["users"]
print(type(user_details))

