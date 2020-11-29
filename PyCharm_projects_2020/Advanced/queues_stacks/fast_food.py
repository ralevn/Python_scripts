from collections import deque

food_quantity = int(input())
orders = deque(int(ors) for ors in input().split(' '))

print(max(orders))

for _ in range(len(orders)):
    order = orders[0]
    if order <= food_quantity:
        food_quantity -= order
        orders.popleft()
    else:
        break

if orders:
    print(f'Orders left:', *orders)
else:
    print('Orders complete')
