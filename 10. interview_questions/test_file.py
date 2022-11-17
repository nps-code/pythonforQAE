text = "AABBCDEFFC"
i=0
list_one = []
for i in range(0, len(text)):
    for j in range(i+1, len(text)):
        if text[i]==text[j]:
            list_one.append(text[i])
print(list_one)



