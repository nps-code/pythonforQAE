""" Uncomment the below code first and execute to know the importance of string format.
"""
# var1 = "Test"
# var2 = 123
# print(var1 + var2)

"""
     1. The syntax is pretty simple. Let's take a template string and then call the .format() method of
     2. that string with some number of positional arguments or keyword arguments, or both.
     3. We use {} as replacement fields in the template.
     4. Then the replacement fields substituted by the arguments or keywords.

"""
print("Hello".format())

text = " Friends"
print("Hello {}".format(text))

var1 = " Test "
var2 = 123
print("{}{}".format(var1, var2))
print("{1}{0}".format(var1, var2))

first_name = "Naresh"
print("Hello, {}{last_name}".format(first_name, last_name=" Padakanti"))

print("Learn {{{}}}".format("Python"))

var1 = "Python"
var2 = 2021
print("Hello {}{} ".format(var2))


def add_name(name):
    txt = "Hello {}"
    txt2 = txt.format(name)
    return txt2


print(add_name("Naresh"))
