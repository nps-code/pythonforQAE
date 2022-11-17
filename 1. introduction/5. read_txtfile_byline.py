file = open(r"D:\1. Naresh\test_data.txt")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()