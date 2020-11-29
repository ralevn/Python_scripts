event_order = input().split('|')

energy = 100
coins = 100

for item in event_order:
    name = item.split('-')[0]
    value = int(item.split('-')[1])
    if name == 'rest':
        if energy + value <= 100:
            energy += value
            print(f'You gained {value} energy.')
        else:
            print(f'You gained {100 - energy} energy.')
            energy = 100
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy - 30 >= 0:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - value > 0:
            coins -= value
            print(f'You bought {name}.')
        else:
            print(f'Closed! Cannot afford {name}.')
            exit()

print(f'Day completed! \nCoins: {coins} \nEnergy: {energy}')