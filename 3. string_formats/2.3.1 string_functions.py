str3 = "Welcome To Python !"

print(len(str3))
print(str3.upper())
print(str3.lower())
print(str3.capitalize())
print(str3.find("To"))
print(str3.isupper())
print(str3.islower())
print(str3.replace("Python", "^^^PYTHON^^^"))


str4 = str3.split()
print(str4)

str5 = "Welcome To Python Python Python Python !"
print(str5.count("Python"))

str6 = "     ??????  Hello Hi How are you  ???????    "
print(str6.strip())
print(str6.strip(' ?'))
print(str6.rstrip(" ?"))
print(str6.lstrip(" ?"))

