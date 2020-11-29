fire_list = input().split('#')
water = int(input())

fire_total = 0

print('Cells:')

fire_dict = {t: int(r) for i in fire_list for t, r in i.split(' = ')}
