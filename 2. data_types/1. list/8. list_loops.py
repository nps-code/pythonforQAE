list_seven = ["HP", "DELL", "LENOVO", "ACER"]
print("Using for loop by item.")
for item in list_seven:
    print(item)

print("Using for loop by range.")
for i in range(len(list_seven)):
    print(list_seven[i])

print("Using while loop.")
i = 0
while i < len(list_seven):
    print(list_seven[i])
    i = i+1

print("Using for loop inline.")
[print(item) for item in list_seven]  # need more understanding on it.
