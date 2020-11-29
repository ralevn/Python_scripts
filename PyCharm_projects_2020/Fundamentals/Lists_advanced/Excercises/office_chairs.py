number_of_rooms = int(input())
room_list = [input().split(' ') for i in range(number_of_rooms)]

free_chairs = 0
is_all_ok = True

print(room_list)

for i in range(len(room_list)):
    chairs = room_list[i][0].count('X')
    taken = int(room_list[i][1])
    if chairs >= taken:
        free_chairs += (chairs - taken)
    else:
        print(f'{taken - chairs} more chairs needed in room {i + 1}')
        is_all_ok = False

if is_all_ok:
    print(f'Game On, {free_chairs} free chairs left')