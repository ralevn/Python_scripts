from collections import defaultdict
guests = defaultdict(list)
unliked_meals = 0

line = input()
while line != 'Stop':
    name = line.split('-')[1]
    meal = line.split('-')[2]
    if line.split('-')[0] == 'Like':
        if meal not in guests[name]:
            guests[name].append(meal)
    if line.split('-')[0] == 'Unlike':
        if name not in guests:
            print(f'{name} is not at the party.')
        elif meal in guests[name]:
            guests[name].remove(meal)
            print(f'{name} doesn\'t like the {meal}.')
            unliked_meals += 1
        elif meal not in guests[name]:
            print(f'{name} doesn\'t have the {meal} in his/her collection.')
    line = input()

ordered_guests = sorted(guests.items(), key= lambda s: (-len(s[1]), s[0]))

for g, m in ordered_guests:
    print(f'{g}:', ', '.join(m))
print(f'Unliked meals: {unliked_meals}')
#print(ordered_guests)