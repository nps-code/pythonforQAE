# list_one = [10.2, 345.98776, 100.0098]
# for num in list_one:
#     print("{:.2f}".format(num))


# list_two = [1, 20, 300, 400]
# for num in list_two:
#     print("{:0>6}".format(num))
#     print("{:0<6}".format(num))

# list_two = [1, -20, 300, 400, -245]
# for num in list_two:
#     print("{:0>+6}".format(num))
#     print("{:0>-6}".format(num))

list_two = [1, -20, 300, 400, -245]
for num in list_two:
    print("{:4>#X}".format(num))
