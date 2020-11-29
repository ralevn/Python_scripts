destination = input()

while destination != 'End':
    budget = int(input())
    saved = 0
    while saved <= budget:
        income = int(input())
        saved += income
    print(f'Going to {destination}')
    destination = input()

