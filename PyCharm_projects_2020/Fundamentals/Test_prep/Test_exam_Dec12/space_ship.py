width_ship = float(input())
length_ship = float(input())
heigth_ship = float(input())
aust_avg_heigth = float(input())

austr_need_space = 2 * 2 * (aust_avg_heigth + 0.4)
ship_space = width_ship * length_ship * heigth_ship
austr_num = int(ship_space / austr_need_space)

if austr_num >= 3 and austr_num <= 10:
    print(f'The spacecraft holds {austr_num} astronauts.')
elif austr_num <3:
    print('The spacecraft is too small.')
elif austr_num > 8:
    print('The spacecraft is too big.')