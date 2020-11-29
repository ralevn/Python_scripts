days_count = int(input())
day_limit = 0.00


for i in range(days_count):
    items = 0
    day_limit += 60
    expense = ''
    while day_limit > 0 and expense != 'Day over':
        expense = input()
        if expense != 'Day over':
            expense = float(expense)
            if expense > day_limit:
                continue
            day_limit -= expense
            if day_limit < 0:
                print(f'Daily limit exceeded! You\'ve bought {items} products.')
                day_limit = 0.00
                break
            elif day_limit == 0:
                items += 1
                print(f'Daily limit exceeded! You\'ve bought {items} products.')
                day_limit = 0.00
                break
            else:
                items += 1
    if expense == 'Day over':
        print(f'Money left from today: {day_limit:.2f}. You\'ve bought {items} products.')

