budget = float(input())
statisti_n = int(input())
dress_unit_cost = float(input())
dress_all_cost = 0.0

decor = budget * 0.1
if statisti_n > 150:
    dress_all_cost = dress_unit_cost * statisti_n * 0.9
else:
    dress_all_cost = dress_unit_cost * statisti_n

if dress_all_cost + decor <= budget:
    print(f'Action!\nWingard starts filming with {budget - (dress_all_cost + decor):.2f} leva left.' )
else:
    print(f'Not enough money!\nWingard needs {(dress_all_cost + decor) - budget:.2f} leva more.')