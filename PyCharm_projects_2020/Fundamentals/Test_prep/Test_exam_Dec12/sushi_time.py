import math
sushi_type = input()
restaurant_name = input()
plate_num = int(input())
delivery = input()

sushi_price = 0.00

if restaurant_name == 'Sushi Zone':
    if sushi_type == 'sashimi':
        sushi_price = 4.99
    if sushi_type == 'maki':
        sushi_price = 5.25
    if sushi_type == 'uramaki':
        sushi_price = 5.99
    if sushi_type == 'temaki':
        sushi_price = 4.29
elif restaurant_name == 'Sushi Time':
    if sushi_type == 'sashimi':
        sushi_price = 5.49
    if sushi_type == 'maki':
        sushi_price = 4.69
    if sushi_type == 'uramaki':
        sushi_price = 4.49
    if sushi_type == 'temaki':
        sushi_price = 5.19
elif restaurant_name == 'Sushi Bar':
    if sushi_type == 'sashimi':
        sushi_price = 5.25
    if sushi_type == 'maki':
        sushi_price = 5.55
    if sushi_type == 'uramaki':
        sushi_price = 6.25
    if sushi_type == 'temaki':
        sushi_price = 4.75
elif restaurant_name == 'Asian Pub':
    if sushi_type == 'sashimi':
        sushi_price = 4.50
    if sushi_type == 'maki':
        sushi_price = 4.80
    if sushi_type == 'uramaki':
        sushi_price = 5.50
    if sushi_type == 'temaki':
        sushi_price = 5.50
else:
    print(f'{restaurant_name} is invalid restaurant!')
    exit()

total_sum = (sushi_price * plate_num)

if delivery =='Y':
    total_sum *= 1.20

print(f'Total price: {math.ceil(total_sum)} lv.')