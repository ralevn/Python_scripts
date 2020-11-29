budget = float(input())

star_price = 5.69
angel_price = 8.49
lights_price = 11.20
wreath_price = 15.50
candle_price = 3.59

product = input()
product_count = 0
sum_spent = 0

while product != 'Finish' and budget - sum_spent >= 0:
    if budget - sum_spent <= 0:
        print(f'Not enough money! You need {abs(sum_spent - budget):.2f}lv more.')
        print(f'"{product_count - 1} items -> {sum_spent:.2f}lv spent.')
        exit()
    if product_count % 3 != 0:
        if product == 'Star':
            sum_spent += star_price
        elif product == 'Angel':
            sum_spent += angel_price
        elif product == 'Lights':
            sum_spent += lights_price
        elif product == 'Wreath':
            sum_spent += wreath_price
        elif product == 'Candle':
            sum_spent += candle_price
    elif product_count % 3 == 0:
        if product == 'Star':
            sum_spent += star_price * 0.70
        elif product == 'Angel':
            sum_spent += angel_price * 0.70
        elif product == 'Lights':
            sum_spent += lights_price * 0.70
        elif product == 'Wreath':
            sum_spent += wreath_price * 0.70
        elif product == 'Candle':
            sum_spent += candle_price * 0.70
    product = input()
    product_count += 1

if product == 'Finish':
    print(f'Congratulations! You bought everything!')
    print(f'{product_count} items -> {sum_spent:.2f}lv spent.')

