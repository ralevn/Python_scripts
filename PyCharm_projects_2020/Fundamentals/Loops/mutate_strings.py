text1 = input()
text2 = input()

textlen = len(text2)
temptext1 = ''
temptext2 = ''
i = 1

while i <= textlen:
    temptext1 = text2[:i] + text1[i:]
    if i == 1 and temptext1 != text1:
        print (temptext1)
    i += 1
    temptext2 = text2[:i] + text1[i:]
    if temptext2 == temptext1:
        continue
    else:
        print(temptext2)
