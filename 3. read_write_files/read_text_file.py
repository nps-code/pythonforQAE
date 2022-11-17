"""
    1. 'open' is the inbuilt method to access the text files.
    2. We need to pass the path of the text file as an argument.
    3. Always close the file at the end to avoid any memory leaks.
"""
text_file = open("read_test.txt")  # Creating an object for open
print(text_file.read())  # To read entire text in the file.
print(text_file.readline())  # To read text in the file line by line (first line).
print(text_file.readline())  # To read text in the file line by line (second line).
print(text_file.read(3))  # To read the required text in the file please note going to next line is considered as one char.
text_file.close()
