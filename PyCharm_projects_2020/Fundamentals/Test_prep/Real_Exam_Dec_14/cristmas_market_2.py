budget = float(input())

star_price = 5.69
angel_price = 8.49
lights_price = 11.20
wreath_price = 15.50
candle_price = 3.59

product = input()
product_count = 0
sum_spent = 0

last_price = 0.00

while product != 'Finish':
    product_count += 1
    if product_count % 3 != 0:
        if product == 'Star':
            sum_spent += star_price
            last_price = star_price
        elif product == 'Angel':
            sum_spent += angel_price
            last_price = angel_price
        elif product == 'Lights':
            sum_spent += lights_price
            last_price = lights_price
        elif product == 'Wreath':
            sum_spent += wreath_price
            last_price = wreath_price
        elif product == 'Candle':
            sum_spent += candle_price
            last_price = candle_price
    else:
        if product == 'Star':
            sum_spent += star_price * 0.70
            last_price = star_price * 0.70
        elif product == 'Angel':
            sum_spent += angel_price * 0.70
            last_price = angel_price * 0.70
        elif product == 'Lights':
            sum_spent += lights_price * 0.70
            last_price = lights_price * 0.70
        elif product == 'Wreath':
            sum_spent += wreath_price * 0.70
            last_price = wreath_price * 0.70
        elif product == 'Candle':
            sum_spent += candle_price * 0.70
            last_price = candle_price * 0.70
    if budget - sum_spent < 0:
        print(f'Not enough money! You need {abs(budget - sum_spent):.2f}lv more.')
        print(f'{product_count - 1} items -> {sum_spent - last_price:.2f}lv spent.')
        exit()
    else:
        product = input()

if product == 'Finish':
    print(f'Congratulations! You bought everything!')

print(f'{product_count} items -> {sum_spent:.2f}lv spent.')