guest_sum = int(input())

total_guests = 0
total_sum = 0

group_count = input()
while group_count != 'The restaurant is full':
    group_count_num = int(group_count)
    total_guests += group_count_num
    group_sum = 0
    if group_count_num < 5:
        group_sum = group_count_num * 100
    elif group_count_num >= 5:
        group_sum = group_count_num * 70

    total_sum += group_sum
    group_count = input()

if total_sum >= guest_sum:
    print(f'You have {total_guests} guests and {total_sum - guest_sum} leva left.')
else:
    print(f'You have {total_guests} guests and {total_sum} leva income, but no singer.')