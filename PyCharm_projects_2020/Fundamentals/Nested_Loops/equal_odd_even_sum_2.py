num_1 = int(input()) ## six digit always less that num_2
num_2 = int(input()) ## six digit

for num in range(num_1, num_2 + 1, 1):
    str_num = str(num)
    sum_odd = sum_even = 0
    for ind, digit in enumerate(str_num):
        int_digit = int(digit)
        if ind % 2 != 0:
            sum_odd += int(int_digit)
        else:
            sum_even += int(int_digit)
    if sum_even == sum_odd:
        print(num, end=' ')