contestants = int(input())

cookies_count = 0
cakes_count = 0
waffels_count = 0

for i in range(contestants):
    contestant_name = input()
    cont_cookies = 0
    cont_cakes = 0
    cont_waffels = 0
    pastry_type = ''

    while pastry_type != 'Stop baking!':
        pastry_type = input()
        if pastry_type != 'Stop baking!':
            count = int(input())
        if pastry_type == 'cookies':
            cookies_count += count
            cont_cookies += count
        elif pastry_type == 'cakes':
            cakes_count += count
            cont_cakes += count
        elif pastry_type == 'waffles':
            waffels_count += count
            cont_waffels += count
        elif pastry_type == 'Stop baking!':
           break

    print(f'{contestant_name} baked {cont_cookies} cookies, {cont_cakes} cakes and {cont_waffels} waffles.')

all_bakery = cookies_count + cakes_count + waffels_count
total_sum = 1.50 * cookies_count + 7.80 * cakes_count + 2.30 * waffels_count
print(f'All bakery sold: {all_bakery}')
print(f'Total sum for charity: {total_sum:.2f} lv.')