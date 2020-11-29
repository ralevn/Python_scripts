given_string = input()

i_string = given_string.lower()
text1 = 'sand'
text2 = 'water'
text3 = 'fish'
text4 = 'sun'

i = i_string.count(text1) + \
    i_string.count(text2) + \
    i_string.count(text3) + \
    i_string.count(text4)

print(i)