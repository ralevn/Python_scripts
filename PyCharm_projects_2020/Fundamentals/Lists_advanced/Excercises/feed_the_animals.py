def get_command(text):
    if text[0] == 'L':
        text_li = text.split(' ')
    else:
        text_li = text.split(':')
    return text_li


def sort_dict_1 (dictionary):
    return dict(sorted(dictionary.items(), key=lambda i: (-i[1], i[0])))


def sort_dict_2(dictionary):
    return dict(sorted(dictionary.items(), key=lambda i: -len(i[1])))


command = get_command(input())

animals_limits = {}
areas = {}

while command[0] != 'Last':
    name = command[1]
    limit = int(command[2])
    area = command[3]

    if command[0] == 'Add':
        if name not in animals_limits:
            animals_limits[name] = limit
        else:
            animals_limits[name] += int(command[2])
        if area not in areas:
            areas[area] = []
        if name not in areas[area]:
            areas[area].append(name)
    if command[0] == 'Feed':
        if name in animals_limits:
            if animals_limits[name] - limit > 0:
                animals_limits[name] -= limit
            else:
                print(f'{name} was successfully fed')
                del animals_limits[name]
                for i in areas:
                    if name in areas[i]:
                        areas[i].remove(name)
    command = get_command(input())

animals_limits = sort_dict_1(animals_limits)
areas = sort_dict_2(areas)

print('Animals:')
for i in animals_limits:
    print(f'{i} -> {animals_limits[i]}g')

print('Areas with hungry animals:')
for i in areas:
    if len(areas[i]) > 0:
        print(f'{i} : {len(areas[i])}')