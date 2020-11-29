energy = int(input())
battles_won = 0

command = input()
while command != 'End of battle':
    distance = int(command)
    if energy - distance >= 0:
        energy -= distance
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        exit()
    command = input()

if energy >= 0:
    print(f'Won battles: {battles_won}. Energy left: {energy}')
