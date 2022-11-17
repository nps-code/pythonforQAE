"""
    1. We can use with statement to open a text file where we need not mention close at the end of the file as its taken
       care automatically unlike using just open method.
    2. We can intimate Python whether we are opening the file in read or write mode.
"""
with open("write_test.txt", 'r') as reader:  # To open in read mode.
    content = reader.readlines()
    reversed(content)
with open("write_test.txt", 'w') as writer:
    for line in reversed(content):
        writer.write(line)
