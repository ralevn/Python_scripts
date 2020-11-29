text = input()

emoticons = []

for i in range(len(text)):
    if text[i] == ':':
        emoticons.append((text[i], text[i + 1]))

for i, j in emoticons:
    print(i,j, sep='')