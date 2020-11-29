engine_power = int(input())
place = input()
eco = input()

tax_rate = 0.00
if place == 'Sofia':
    if engine_power <= 37:
        tax_rate = 1.43
    elif 38 <= engine_power <= 55:
        tax_rate = 1.50
    elif engine_power > 55:
        tax_rate = 2.68
elif place == 'Vidin':
    if engine_power <= 37:
        tax_rate = 1.34
    elif 38 <= engine_power <= 55:
        tax_rate = 1.40
    elif engine_power > 55:
        tax_rate = 2.54
elif place == 'Varna':
    if engine_power <= 37:
        tax_rate = 1.37
    elif 38 <= engine_power <= 55:
        tax_rate = 1.40
    elif engine_power > 55:
        tax_rate = 2.57

discount_rate = 0.00
if eco == 'Euro 4':
    discount_rate = 0.15
elif eco == 'Euro 5':
    discount_rate = 0.17
elif eco == 'Euro 6':
    discount_rate = 0.20

## print(f'eco = {eco}: discount = {discount_rate}: engine = {engine_power}: tax rate = {tax_rate}')

discount = (engine_power * tax_rate) * discount_rate
tax = (engine_power * tax_rate) -discount

print(f'{tax:.2f} lv')