"""
We have different ways to format given string.
"""
str1 = "Python course"
str2 = "2022"
# Using concatenate operator
print("Welcome to"+str1+str2)

# Using percentiles (%s) in front of the variables.
print("Welcome to %s, %s" % (str1, str2))
print("Learn %s, %s" % (str2, "Strongly."))

# Using format method.
print("Hello, lets learn {} in {}".format(str1, str2))
# The same method with index.
print("Hello, in {1}, lets learn {0} ".format(str1, str2))
print("Hello, in {year}, lets learn {course} ".format(course=str1, year=str2))

