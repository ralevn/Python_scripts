fruit_type =input()
week_day = input()
quantity = float(input())

price = 0.00

if week_day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit_type == 'banana': price = 2.50
    elif fruit_type == 'apple': price = 1.20
    elif fruit_type == 'orange': price = 0.85
    elif fruit_type == 'grapefruit': price = 1.45
    elif fruit_type == 'kiwi': price = 2.70
    elif fruit_type == 'pineapple': price = 5.50
    elif fruit_type == 'grapes': price = 3.85
    else: price = 0
elif week_day in ['Saturday', 'Sunday']:
    if fruit_type == 'banana': price = 2.70
    elif fruit_type == 'apple': price = 1.25
    elif fruit_type == 'orange': price = 0.90
    elif fruit_type == 'grapefruit': price = 1.60
    elif fruit_type == 'kiwi': price = 3.00
    elif fruit_type == 'pineapple': price = 5.60
    elif fruit_type == 'grapes': price = 4.20
    else: price = 0

cost = price * quantity
if price != 0.00:
    print(f'{cost:.2f}')
else:
    print('error')

