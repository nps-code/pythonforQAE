"""
    1. json package is available by default in Python.
    2. json.loads is method used to read the data of a json string.
    3. It converts the json data to dictionary by default to use further.
    4. If the json data happens to be in another format like list, it will convert the response to list automatically.
"""
import json

# sample json
student = '{"name" : "Cherry", "grade" : "7", "sub" : ["English", "Math", "Science"], "flag": true}'

student_data = json.loads(student)  # It converts the json to dictionary data type.
print(type(student_data))
print(student_data)

print(type(student_data)["name"])
print((student_data["sub"]))
print(student_data["sub"][1])
