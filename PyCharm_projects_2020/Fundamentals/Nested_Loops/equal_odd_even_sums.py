num_1 = int(input()) ## six digit always less that num_2
num_2 = int(input()) ## six digit

for i in range(num_1, num_2 + 1, 1):
    string_num = str(i)
    sum_odd = sum_even = 0
    for p in range(len(string_num)):
        if p % 2 != 0:
            sum_odd += int(string_num[p - 1])
        else:
            sum_even += int(string_num[p - 1])
    if sum_even == sum_odd:
        print(string_num, end=' ')

