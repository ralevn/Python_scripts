def numbers_in_group(n, li):
    n_min = (n - 1) * 10
    n_max = n * 10
    li_new = [v for v in li if n_min < v <= n_max]
    return li_new


def number_of_groups(li):
    if max(li) % 10 == 0:
        return max(li) // 10
    else:
        return (max(li) // 10) + 1


list_of_numbers = [int(n) for n in input().split(', ')]

for i in range(1, number_of_groups(list_of_numbers) + 1):
    print(f'Group of {i}0\'s:', numbers_in_group(i, list_of_numbers))

