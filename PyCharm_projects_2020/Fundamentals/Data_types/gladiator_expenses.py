lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

cost = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        cost += helmet_price
    if i % 3 == 0:
        cost += sword_price
    if i % 6 == 0:
        cost += shield_price
    if i % 12 == 0:
        cost += armor_price

print(f'Gladiator expenses: {cost:.2f} aureus')