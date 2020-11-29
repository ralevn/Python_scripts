name = ''
win_name = ''
win_name_sum = 0
name_sum = 0


while name != 'STOP':
    name = input()
    name_sum = 0
    for i in range(len(name)):
        name_sum += ord(name[i])
        if name_sum > win_name_sum:
            win_name_sum = name_sum
            win_name = name

print(f'Winner is {win_name} - {win_name_sum}!')

