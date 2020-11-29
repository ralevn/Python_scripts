stock = {}
line = input()

while line != 'statistics':
    item = line.split(': ')[0]
    quantity = int(line.split(': ')[1])
    if item not in stock:
        stock[item] = quantity
    else:
        stock[item] += quantity
    line = input()

print('Products in stock:')
for i in stock:
    print(f'- {i}: {stock[i]}')

print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')
