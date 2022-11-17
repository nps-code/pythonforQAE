fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print("way 1: ")
print("==========================================================")
name = [fruit for fruit in fruits]
print(name)

print("==========================================================")
print("way 2: ")
[print(item) for item in fruits]

print("==========================================================")
print("appending the fruits to a new list using for loop ")
new_list = []
for f in fruits:
    if 'a' in f:
        new_list.append(f)
print(new_list)

print("==========================================================")
print("appending the fruits to a new list using comprehensive list.")
new_list = [f for f in fruits if 'a' in f]
print(new_list)

