initial_ponts = int(input())

bullseye = False
target_section = ''
points = 0
counter = 0

while initial_ponts > 0 and bullseye == False:
    counter += 1
    target_section = input()
    if target_section == 'bullseye':
        bullseye = True
        break
    points = int(input())
    if target_section == 'number section':
        initial_ponts -= points
    elif target_section == 'double ring':
        initial_ponts -= points * 2
    elif target_section == 'triple ring':
        initial_ponts -= points * 3

if  initial_ponts == 0:
    print(f'Congratulations! You won the game in {counter} moves!')
elif bullseye == True:
    print(f'Congratulations! You won the game with a bullseye in {counter} moves!')
elif initial_ponts < 0:
    print(f'Sorry, you lost. Score difference: {abs(initial_ponts)}.')