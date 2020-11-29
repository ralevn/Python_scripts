budget = int(input())
towel_price = float(input())
discount = int(input())

umbrell_price = (2 * towel_price) / 3
slippers_price = umbrell_price * 0.75
bag_price = (towel_price + slippers_price) / 3

total_cost = ( umbrell_price + slippers_price + bag_price + towel_price) * ( ( 100 - discount ) / 100)

if budget >= total_cost:
    print(f'Annie\'s sum is {total_cost:.2f} lv. She has {budget - total_cost:.2f} lv. left.')
else:
    print(f'Annie\'s sum is {total_cost:.2f} lv. She needs {total_cost - budget:.2f} lv. more.')