number_list = [int(n) for n in input().split(' ')]
n = int(input())
executed =[]

skip_n = n - 1

while len(number_list) > 1:
    executed.append(number_list.pop(skip_n))
    skip_n = (skip_n + n - 1) % len(number_list)

print(executed + number_list)
