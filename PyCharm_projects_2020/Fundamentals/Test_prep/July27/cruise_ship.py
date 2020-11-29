cruise_type = input()
cabin_type = input()
nights = int(input())

price = 0.00

if cruise_type == 'Mediterranean':
    if cabin_type == 'standard cabin':
        price = 27.50
    elif cabin_type == 'cabin with balcony':
        price = 30.20
    else:
        price = 40.50
elif cruise_type == 'Adriatic':
    if cabin_type == 'standard cabin':
        price = 22.99
    elif cabin_type == 'cabin with balcony':
        price = 25.00
    else:
        price = 34.99
else:
    if cabin_type == 'standard cabin':
        price = 23.00
    elif cabin_type == 'cabin with balcony':
        price = 26.60
    else:
        price = 39.80

cost = nights * price * 4

if nights > 7:
    cost *= 0.75

print(f'Annie\'s holiday in the {cruise_type} sea costs {cost:.2f} lv.')