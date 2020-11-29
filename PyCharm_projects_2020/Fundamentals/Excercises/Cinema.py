type = input()
rows, cols = int(input()), int(input())

if type == 'Premiere':
    income = rows * cols * 12.00
elif type == 'Normal':
    income = rows * cols * 7.50
elif type == 'Discount':
    income = rows * cols * 5.00

print(f'{income:.2f} leva')

