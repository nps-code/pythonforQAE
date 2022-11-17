"""
1. Variable is name given to an object or a value in any programming language.
2. In Python, we can simply assign a value or object to a variable without
    declaring the types of it explicitly.
3. Python converts it internally based on the value assigned.
4. Variable name must start with a letter or underscore(_) only.
    It is not allowed to start with any number or other special character.
5. Variable names are case-sensitive .
6. Any of Python's reserve words can't be used as variables.
"""

# Variable assignment.
# 1variable = "test"
x = 10
y = "TEST"
z = 12.5
i = True
print(x, y, z, i)
print("-------------------------------------------")

# To know type and location id.
print(type(y))
print(id(y))
print("-------------------------------------------")

# Assigning variables in one go.
a, b, c, d = 5, 10.5, 7, 8
print(a, b, c, d)
print("-------------------------------------------")

# Variable is case-sensitive
test_var = "Java"
TEST_VAR = "Python"
print(test_var)
print(TEST_VAR)
