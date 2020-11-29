quantity = int(input())
days = int(input())

# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garlands = 3
# tree_lights = 15

current_day = 1
cost = 0
spirit = 0

# condition = current_day <= days

while current_day <= days:
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        cost += 2 * quantity
        spirit += 5
    if current_day % 3 == 0:
        cost += 8 * quantity
        spirit += 13
    if current_day % 5 == 0:
        cost += 15 * quantity
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        cost += 23
        if current_day == days:
            spirit -= 30
    current_day += 1

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')


