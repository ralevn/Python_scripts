list_1 = [a for a in input().split(', ')]
list_2 = input()

new_list = [i for i in list_1 if i in list_2]

print(new_list)