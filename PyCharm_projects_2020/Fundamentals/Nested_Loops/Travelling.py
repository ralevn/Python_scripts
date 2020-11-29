country = input()

while country != 'End':
    need_sum = float(input())
    saved_sum = 0

    while saved_sum < need_sum:
        money = float(input())
        saved_sum += money
    print(f'Going to {country}!')
    country = input()