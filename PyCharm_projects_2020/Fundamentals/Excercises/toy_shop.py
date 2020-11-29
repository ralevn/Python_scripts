trip_price = float(input())
puzzel_n, dolls_n, teddys_n, minons_n, truck_n = int(input()), int(input()), int(input()), int(input()), int(input())

if (puzzel_n + teddys_n + minons_n + truck_n + dolls_n) > 49:
    order_profit = ((puzzel_n * 2.60) + (dolls_n * 3.00) + (teddys_n * 4.10) + (minons_n * 8.20) + (truck_n * 2.00)) * 0.75
else: order_profit = (puzzel_n * 2.60) + (dolls_n * 3.00) + (teddys_n * 4.10) + (minons_n * 8.20) + (truck_n * 2.00)

# print(puzzel_n + teddys_n + minons_n + truck_n + dolls_n)
# print(order_profit)

money_left = order_profit * 0.90
# print(money_left)

if money_left  >= trip_price:
    diff = money_left - trip_price
    print (f'Yes! %.2f lv left.' %(diff))
else: diff = trip_price - money_left; print(f'Not enough money! %.2f lv needed.' %(diff))