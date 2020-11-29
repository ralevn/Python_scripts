budget = float(input())
season = input()
count_fishers = int(input())
boat_price = 0
discount = 0
discount_2 =0

if season == 'Spring': boat_price = 3000
elif season in ['Summer', 'Autumn']: boat_price = 4200
elif season == 'Winter': boat_price = 2600

if count_fishers <= 6: discount = 0.9
elif 7 <= count_fishers <= 11: discount = 0.85
elif count_fishers >= 12: discount = 0.75

if count_fishers % 2 == 0 and season != 'Autumn': discount_2 = 0.95
else: discount_2 = 1

cost = (boat_price * discount) * discount_2

if budget >= cost:
    print(f'Yes! You have {(budget - cost):.2f} leva left.')
else:
    print(f'Not enough money! You need {(cost - budget):.2f} leva.')