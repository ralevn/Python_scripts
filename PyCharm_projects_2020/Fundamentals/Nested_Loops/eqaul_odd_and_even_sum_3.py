num_1 = int(input()) ## six digit always less that num_2
num_2 = int(input()) ## six digit

sum_odd = sum_even = 0

for i in range(num_1, num_2 + 1, 1):
    string_num = str(i)
    sum_odd = int(string_num[0]) + int(string_num[2]) + int(string_num[4])
    sum_even = int(string_num[1]) + int(string_num[3])  + int(string_num[5])
    if sum_even == sum_odd:
        print(string_num, end=' ')