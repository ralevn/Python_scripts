fire_list = input().split('#')
water = int(input())

fire_total = 0

print('Cells:')

for item in fire_list:
    fire_type = item.split(' = ')[0]
    cell_value = int(item.split(' = ')[1])
    if (fire_type == 'High') and (81 <= cell_value <= 125) and (water >= cell_value):
        water -= cell_value
        print(f' - {cell_value}')
        fire_total += cell_value
    elif (fire_type == 'Medium') and (51 <= cell_value <= 80) and (water >= cell_value):
        water -= cell_value
        print(f' - {cell_value}')
        fire_total += cell_value
    elif (fire_type == 'Low') and (1 <= cell_value <= 50) and (water >= cell_value):
        water -= cell_value
        print(f' - {cell_value}')
        fire_total += cell_value

effort = fire_total * 0.25

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire_total}')

def map_command (comm, lis):
    if comm[0] == 'exchange':
        lis = exchange(int(comm[1]), lis)
    elif comm[0] == 'max' or comm[0] == 'min':
        print (max_min_even_odd(f'{comm[0]} {comm[1]}', lis))
    elif comm[0] == 'firs' or comm[0] == 'last':
        print (first_last_even_odd(comm[0], comm[1], comm[2], lis))




