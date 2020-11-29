products = {}

buys = input().split(' ')
while buys[0] != 'buy':
    name = buys[0]
    price = float(buys[1])
    quantity = int(buys[2])
    if name not in products:
        products[name] = [price, quantity]
    else:
        quantity += products[name][1]
        products[name] = [price, quantity]
    buys = input().split()

for p in products:
    price = products[p][0]
    quantity = products[p][1]
    print(f'{p} -> {price * quantity:.2f}')
