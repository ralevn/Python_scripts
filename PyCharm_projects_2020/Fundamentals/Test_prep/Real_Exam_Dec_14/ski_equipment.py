budget = float(input())
ski_price = float(input())
sticks_price = float(input())

ski_boots_price = ski_price * 0.40
ski_dress = ski_price * 1.4

if ski_price + ski_boots_price + ski_dress > 800:
    sticks_price = 0

total_cost =  ski_price + ski_boots_price + ski_dress + sticks_price

if budget >= total_cost:
    print(f'Angel\'s sum is {total_cost:.2f} lv. He has {budget - total_cost:.2f} lv. left.')
else:
    print(f'Not enough money! You need {total_cost - budget:.2f} leva more!')