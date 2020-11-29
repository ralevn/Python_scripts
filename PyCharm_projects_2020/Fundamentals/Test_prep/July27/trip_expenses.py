days = int(input())
reminder = 0

for i in range(days):
    balance = 60 + reminder
    item_count = 0
    line = input()

    while True:
        if line == "Day over":
            print(f"Money left from today: {balance:.2f}. You've bought {item_count} products.")
            reminder = balance
            break

        item_price = float(line)
        if item_price <= balance:
            item_count = item_count + 1
            balance = balance - item_price
        if balance == 0:
            print(f"Daily limit exceeded! You've bought {item_count} products.")
            break
        line = input()



