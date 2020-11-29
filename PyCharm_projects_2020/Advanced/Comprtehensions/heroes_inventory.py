names_init = input().split(', ')

names_item = {name: [] for name in names_init}
names_cost = {name: 0 for name in names_init}

lines = input()
while lines != 'End':
    name, item, cost = lines.split('-')[0], lines.split('-')[1], int(lines.split('-')[2])
    if item not in names_item[name]:
        names_item[name].append(item)
        names_cost[name] += cost
    lines = input()

for n in names_init:
    print(f'{n} -> Items: {len(names_item[n])}, Cost: {names_cost[n]}')