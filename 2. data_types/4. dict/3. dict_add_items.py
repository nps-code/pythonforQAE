dict_three = {
    "emp_id": 12345,
    "emp_name": "Naresh",
    "org_name": "Testing Comp"
}

dict_three.update({"org_name": "DevOps Comp"})
dict_three.update({"loc": "Hyd"})
# OR
# dict_three["loc"] = "Hyd"
print(dict_three)
