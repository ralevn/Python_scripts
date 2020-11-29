cities = {}

inp_city = input()
while inp_city != 'Sail':
    city = inp_city.split('||')[0]
    population = int(inp_city.split('||')[1])
    gold = int(inp_city.split('||')[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
    inp_city = input()

event = input()
while event != 'End':
    if event.split('=>')[0] == 'Plunder':
        town = event.split('=>')[1]
        people = int(event.split('=>')[2])
        p_gold = int(event.split('=>')[3])
        if (cities[town][0] - people > 0) and (cities[town][1] - p_gold > 0):
            cities[town][0] -= people
            cities[town][1] -= p_gold
            print(f'{town} plundered! {p_gold} gold stolen, {people} citizens killed.')
        elif (cities[town][0] - people <= 0) and (cities[town][1] - p_gold > 0):
            print(f'{town} plundered! {p_gold} gold stolen, {cities[town][0]} citizens killed.')
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
        elif (cities[town][0] - people > 0) and (cities[town][1] - p_gold <= 0):
            print(f'{town} plundered! {cities[town][1]} gold stolen, {people} citizens killed.')
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
        elif (cities[town][0] - people <= 0) and (cities[town][1] - p_gold <= 0):
            print(f'{town} plundered! {cities[town][1]} gold stolen, {cities[town][0]} citizens killed.')
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif event.split('=>')[0] == 'Prosper':
        town = event.split('=>')[1]
        gold = int(event.split('=>')[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
            event = input()
            continue
        else:
            cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
    event = input()

if len(cities) > 0:
    ordered_cities = sorted(cities.items(), key=lambda s: (-s[1][1], s[0]))
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for t, i in ordered_cities:
        print(f'{t} -> Population: {i[0]} citizens, Gold: {i[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")