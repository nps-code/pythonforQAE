# print("{:K>6}".format(25))
# print("{0:{1}>{2}}".format(25, "K", 8))


def checker(num, formatter, spaces):
    f = "{0:{1}>{2}}".format(num, formatter, spaces)
    return f


print(checker(125, "Q", 8))
