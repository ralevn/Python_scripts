food_money_daily = float(input())
souv_money_daily = float(input())
hotel_money_daily = float(input())

travel_expense = ((420 / 100) * 7) * 1.85
accomodation_expense = hotel_money_daily * 0.9 + hotel_money_daily * 0.85 + hotel_money_daily * 0.8

total_expenes = (food_money_daily * 3) + (souv_money_daily * 3) + accomodation_expense + travel_expense

print(f'Money needed: {total_expenes:.2f}')