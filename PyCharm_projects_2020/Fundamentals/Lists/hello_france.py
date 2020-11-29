product_list = input().split('|')
int_budget = float(input())
budget = int_budget
bought_items = []
new_prices = []

for product in product_list:
    product_name = product.split('->')[0]
    product_price = float(product.split('->')[1])
    if product_name == 'Clothes' and product_price <= 50.00 and product_price <= budget:
        budget -= product_price
        bought_items.append(product_price)
        new_prices.append(f'{product_price * 1.4:.2f}')
    elif product_name == 'Shoes' and product_price <= 35.00 and product_price <= budget:
        budget -= product_price
        bought_items.append(product_price)
        new_prices.append(f'{product_price * 1.4:.2f}')
    elif product_name == 'Accessories' and product_price <= 20.50 and product_price <= budget:
        budget -= product_price
        bought_items.append(product_price)
        new_prices.append(f'{product_price * 1.4:.2f}')

profit = sum([float(n) for n in new_prices]) - sum(bought_items)
print(*new_prices)
print(f'Profit: {profit:.2f}')

if int_budget + profit >= 150:
    print('Hello, France!')
else:
    print('Time to go.')