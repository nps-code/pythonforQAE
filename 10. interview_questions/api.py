#   1.How to find david email. refer user_details json.
import json
with open("D:\\1. Naresh\\1. My Learning\\0.1 Training Material\\Test Files\\user_details.json") as file:
    data = json.load(file)

print(data)
print(type(data))   # It returns the data in the form of dictionary.
#  To find david email.
print(data["users"])    # Value of key 'users' is a list.
print(type(data["users"][3]))  # Every item in the list is a dictionary again.
print(data["users"][3]["emailAddress"])  # Hence, we are accessing email by using keyword given.
