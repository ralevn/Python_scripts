money_need = float(input())
months = int(input())

current_money = 0.00

for m in range(1, months + 1):
    if m % 2 != 0 and m != 1:
        current_money *= 0.84
    elif m % 4 == 0:
        current_money *= 1.25
        #if current_money >= money_need:
            #break
    current_money += money_need * 0.25
    #if current_money >= money_need:
        #break

if current_money >= money_need:
    print(f'Bravo! You can go to Disneyland and you will have {current_money - money_need:.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {money_need - current_money:.2f}lv. more.')