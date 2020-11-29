def find_index_right(start, jump, listi):
    ind = start + jump
    if ind > len(listi):
        while ind >= len(listi):
            ind -= len(listi)
    return ind


def find_index_left(start, jump, listi):
    ind = start - jump
    if ind < 0:
        while ind < 0:
            ind += len(listi)
    return ind


targets = [int(n) for n in input().split('|')]
points = 0

commands = input()
while commands != 'Game over':
    if commands.split('@')[0] == 'Shoot Left':
        start_ix = int(commands.split('@')[1])
        length = int(commands.split('@')[2])
        if 0 <= start_ix <= len(targets) - 1:
            ix = find_index_left(start_ix, length, targets)
            if targets[ix] - 5 >= 0:
                targets[ix] -= 5
                points += 5
            else:
                points += targets[ix]
                targets[ix] = 0
    elif commands.split('@')[0] == 'Shoot Right':
        start_ix = int(commands.split('@')[1])
        length = int(commands.split('@')[2])
        if 0 <= start_ix <= len(targets) - 1:
            ix = find_index_right(start_ix, length, targets)
            if targets[ix] - 5 >= 0:
                targets[ix] -= 5
                points += 5
            else:
                points += targets[ix]
                targets[ix] = 0
    elif commands.split('@')[0] == 'Reverse':
        targets.reverse()
    commands = input()

targets = [str(n) for n in targets]
print(' - '.join(targets))
print(f'Iskren finished the archery tournament with {points} points!')