command = input()
heros = {}

while command != 'End':
    if command.split(' ')[0] == 'Enroll':
        hero_name = command.split(' ')[1]
        if hero_name not in heros:
            heros[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')
    if command.split(' ')[0] == 'Learn':
        hero_name = command.split(' ')[1]
        spell = command.split(' ')[2]
        if hero_name not in heros:
            print(f'{hero_name} doesn\'t exist.')
        else:
            if spell in heros[hero_name]:
                print(f'{hero_name} has already learnt {spell}.')
            else:
                heros[hero_name].append(spell)
    if command.split(' ')[0] =='Unlearn':
        hero_name = command.split(' ')[1]
        spell = command.split(' ')[2]
        if hero_name not in heros:
            print(f'{hero_name} doesn\'t exist.')
        else:
            if spell not in heros[hero_name]:
                print(f'{hero_name} doesn\'t know {spell}.')
            else:
                heros[hero_name].remove(spell)
    command = input()

ordered_heros = sorted(heros.items(), key=lambda s: (-len(s[1]), s[0]))

print('Heroes:')

for name, spells in ordered_heros:
    print(f'== {name}:', end=' ' )
    print(', '.join(spells))