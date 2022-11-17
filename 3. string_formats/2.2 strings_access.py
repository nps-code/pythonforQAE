"""
    1. String is stored as list, and we can access letters of it using index.
    2. Index starts from 0.
    3. We can concatenate strings just by using '+' operator.

"""

# Accessing sub strings.
str_one = "Welcome to Python"
print(str_one[0])
print(str_one[0:])
print(str_one[0:7])

#  Concatenation of given strings.
str_two = " in 2022"
str_three = str_one + str_two
print(str_three)

#  Validating sub string in a given string.
str_four = "Python"
print(str_three in str_one)
print(str_three in str_two)
