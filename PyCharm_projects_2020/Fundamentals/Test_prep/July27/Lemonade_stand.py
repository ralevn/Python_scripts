lemon_kg = float(input())
sugar_kg = float(input())
water_l = float(input())

juice_vol = (980 * lemon_kg) + (0.3 * sugar_kg) + (1000 * water_l)
num_of_cups = int(juice_vol / 150)
money = num_of_cups * 1.20

print(f'All cups sold: {num_of_cups}')
print(f'Money earned: {money:.2f}')


