people = {}

command = input()
while command != 'Results':
    if command.split(':')[0] == 'Add':
        name = command.split(':')[1]
        health = int(command.split(':')[2])
        energy = int(command.split(':')[3])
        if name not in people:
            people[name] = [health, energy]
        else:
            people[name][0] += health
    elif command.split(':')[0] == 'Attack':
        attacker = command.split(':')[1]
        defender = command.split(':')[2]
        damage = int(command.split(':')[3])
        if attacker in people and defender in people:
            people[defender][0] -= damage
            if people[defender][0] <= 0:
                print(f'{defender} was disqualified!')
                people.pop(defender)
            people[attacker][1] -= 1
            if people[attacker][1] <= 0:
                print(f'{attacker} was disqualified!')
                people.pop(attacker)
    elif command.split(':')[0] == 'Delete':
        name = command.split(':')[1]
        if name in people:
            people.pop(name)
        if name == 'All':
            people.clear()
    command = input()

print(f'People count: {len(people)}')
ordered_people = sorted(people.items(), key=lambda s: (-s[1][0], s[0]))

for n, v in ordered_people:
    print(f'{n} - {v[0]} - {v[1]}')

