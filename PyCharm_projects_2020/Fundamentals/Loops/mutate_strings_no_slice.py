text1 = input()
text2 = input()

textlen = len(text2)
temptext1 = ''
temptext2 = ''
i = 1

def mutate(num, t1, t2):
    temp1 = ''
    temp2 = ''
    for i in range(num):
        temp1 += t2[i]
    for i in range(num, len(text1)):
        temp2 += t1[i]
    return temp1 + temp2

while i < textlen:
    temptext1 = mutate(i, text1, text2)
    if i == 1 and temptext1 != text1:
        print(temptext1)
    i += 1
    temptext2 = mutate(i, text1, text2)
    if temptext2 == temptext1:
        continue
    else:
        print(temptext2)