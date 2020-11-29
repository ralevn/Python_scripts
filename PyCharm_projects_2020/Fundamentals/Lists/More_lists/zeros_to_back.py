numbers = [int(n) for n in input().split(', ')]

zeroless_list = [n for n in numbers if n !=0]
zero_list = [n for n in numbers if n ==0]
new_list = zeroless_list + zero_list
print(new_list)