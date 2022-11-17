"""
    1. json package is available by default in Python.
    2. json.dumps is method used to read the data which is in Dictionary format and converts it to String.
"""
import json

# sample json
sample_dict = {"country": "India", "code": 91, "flag": True}

print(type(sample_dict))
data = json.dumps(sample_dict)
print(type(data))
print(data)
