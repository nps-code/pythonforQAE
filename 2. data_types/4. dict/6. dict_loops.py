dict_one = {
    "name": "charan",
    "class": 6,
    "roll_no1": 10,
    "roll_no2": 10,
    "roll_no3": 20
    }
count = 0
for item in dict_one:
    if dict_one[item] == 10:
        count = count + 1
print(count)

list_one =[]
for item in dict_one:
    list_one.append(dict_one[item])
print(list_one)


for list_item in list_one:
    print(f" count of {list_item}, {list_one.count(list_item)}")