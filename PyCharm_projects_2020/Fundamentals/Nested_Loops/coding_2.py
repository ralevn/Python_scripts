inp_number = input()
for digit in reversed(inp_number):
    num = int(digit)
    for i in range(num):
        symbol = chr(num + 33)
        print(symbol, end='')
    if num == 0:
        print('ZERO')
    else:
        print()