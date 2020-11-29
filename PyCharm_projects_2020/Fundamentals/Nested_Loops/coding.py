number = input()
num_length = len(number)

for i in range(num_length, 0, -1):
    number_i = int(number[i - 1])
    number_ch_33 = chr(number_i + 33)
    if number_i == 0:
        print('ZERO', end= '')
    else:
        for j in range(number_i):
            print(number_ch_33, end = '')
    print()