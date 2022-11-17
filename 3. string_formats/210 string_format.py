test_variable1 = "Learning Python"
test_variable2 = "Completed in"
year = 2021
# print(test_variable1 + year) #  TypeError: can only concatenate str (not "int") to str
print("{} {}".format(test_variable1, year))
print("{} {} {}".format(test_variable1, test_variable2, year))

