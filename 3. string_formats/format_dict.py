dict_one = {
    "name": "student",
    "class": 6,
    "roll_no": 12345,
    "value": False,
    1: True
    }
print("{[name]}".format(dict_one))
print("{[1]}".format(dict_one))
print("{d[class]}".format(d=dict_one))

mydict = {'1': 'one', 1: '2nd one'}
print("{[1]}".format(mydict))
