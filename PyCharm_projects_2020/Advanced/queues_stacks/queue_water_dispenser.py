from collections import deque

water_volume = int(input())
names = deque()

name = input()
while name != 'Start':
    names.append(name)
    name = input()

line = input().split(' ')
while line[0] != 'End':
    if line[0] != 'refill':
        order = int(line[0])
        if order <= water_volume:
            print (f'{names.popleft()} got water')
            water_volume -= order
        else:
            print(f'{names.popleft()} must wait')
    else:
        water_volume += int(line[1])
    line = input().split(' ')

print(f'{water_volume} liters left')