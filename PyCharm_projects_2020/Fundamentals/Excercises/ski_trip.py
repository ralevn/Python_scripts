days = int(input())
accomodation_type =input()
attitude = input()

room_price = 18.00
apartmet_price = 25.00
president_apartmet_price = 35.00
cost = 0

if accomodation_type == 'room for one person':
    cost = room_price * (days -1 )
elif accomodation_type == 'apartment':
    if days < 10:
        cost = apartmet_price * (days -1) * 0.7
    if 10 <= days <= 15:
        cost = apartmet_price * (days -1) * 0.65
    if days > 15:
        cost = 0.5 * (days -1) * apartmet_price
elif accomodation_type == 'president apartment':
    if days < 10:
        cost = 0.9 * (days -1) * president_apartmet_price
    if 10 <= days <= 15:
        cost = 0.85 * (days -1) * president_apartmet_price
    if days > 15:
        cost = 0.8 * (days -1) * president_apartmet_price

if attitude == 'positive':
    print(f'{cost + cost * 0.25:.2f}')
if attitude == 'negative':
    print(f'{cost - cost * 0.10:.2f}')


