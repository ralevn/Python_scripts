num = int(input())

text1 = 'Leo finally won the Oscar! Leo is happy'
text2 = 'Not even for Wolf of Wall Street?!'
text3 = 'When will you give Leo an Oscar?'
text4 = 'Leo got one already!'


if num == 88:
    print(text1)
elif num == 86:
    print(text2)
elif num != 88 and num != 86 and num < 88:
    print(text3)
else:
    print(text4)