def move_racer(name, from_list, to_list):
    i = 0
    while i < len(from_list):
        if from_list[i] == name:
            to_list.append(from_list.pop(i))
        i += 1


def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda i: (-len(i[1]), i[0])))


command = input().split('->')

roads = {}

while command[0] != 'END':
    road = command[1]
    if command[0] == 'Add':
        racer = command[2]
        if road not in roads:
            roads[road] = [racer]
        else:
            roads[road].append(racer)
    elif command[0] == 'Move':
        racer = command[2]
        new_road = command[3]
        if racer in roads[road]:
            move_racer(racer, roads[road], roads[new_road])
    elif command[0] == 'Close':
        if road in roads:
            del roads[road]
    command = input().split('->')


roads = sort_dict(roads)
print('Practice sessions:')
for i in roads:
    print(i)
    for j in roads[i]:
        print(f'++{j}')