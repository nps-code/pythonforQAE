# *********************************************************************************************************************
# 1. Read the text of a given file using readline method.
# ---------------------------------------------------------------------------------------------------------------------

file = open("test_data.txt")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

# OR

file = open("test_data.txt")
for line in file.readlines():
    print(line)
file.close()

# *********************************************************************************************************************

