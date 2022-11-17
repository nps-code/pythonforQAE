str1 = "Python for QA"
# Gives the starting position of required string.
print(str1.find("QA"))
print(str1.index("QA"))

str2 = "Welcome to Python !"
print(str2.find("QA"))  # We are trying to check the sub string which is not part
# of actual sting, hence it always throw -1 as result.
# print(str2.index("QA"))  # raise ValueError when the substring is not found.


int1 = 123456  # Integer
# print(test_int.find("12"))  # AttributeError: 'int' object has no attribute 'find'
str3 = str(int1)  # Converted to String.
print(type(str3))
print(str3.find("2"))
