number_list = [int(n) for n in input().split(' ')]
n = int(input())
executed =[]

print ('[',end='')
skip_n = n - 1

while len(number_list) > 1:
    print(number_list.pop(skip_n), end=',')
    skip_n = (skip_n + n - 1) % len(number_list)
print(*number_list,']', sep='')
