"""
    1. 'json.dump' is method used to write dictionary data to a json file.
"""
import json

dict1 = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

# the json file where the output must be stored
out_file = open(r"D:\np\test_files\sample_json.json", "w")
json.dump(dict1, out_file, indent=6)
out_file.close()
