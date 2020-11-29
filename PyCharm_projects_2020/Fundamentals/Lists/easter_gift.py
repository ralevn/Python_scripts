gifts = input().split(' ')

command = input()
while command != 'No Money':
    command_li = command.split(' ')
    if command_li[0] == 'OutOfStock':
        gifts = [i if i != command_li[1] else 'None' for i in gifts]
    elif command_li[0] == 'Required':
        if 0 <= int(command_li[2]) <= len(gifts) - 1:
            gifts[int(command_li[2])] = command_li[1]
    else:
        gifts[len(gifts) - 1 ] = command_li[1]
    command = input()

for item in [n for n in gifts if n != 'None']:
    print(item, end=' ')
