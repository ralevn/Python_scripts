floor_num = int(input())
room_num = int(input())
type = ''

for i in range(floor_num, 0, -1):
    if i % 2 == 0:
        type = 'O'
    else:
        type = 'A'
    for j in range(room_num):
        if i == floor_num:
            print('L' + str(i) + str(j) + ' ', end='')
        else:
            print(type + str(i) + str(j) + ' ', end='')
    print()
