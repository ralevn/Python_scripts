width = int(input())
height = int(input())
length = int(input())
priority = input()

volume = width * height * length
tax = 0.00

if volume <= 50:
    print('Luggage tax: 0.00')
    exit()

if priority == 'true':
    if 50 < volume <= 100:
        tax = 0
    elif 100 < volume <= 200:
        tax = 10
    elif 200 < volume <= 300:
        tax = 20
else:
    if 50 < volume <= 100:
        tax = 25
    elif 100 < volume <= 200:
        tax = 50
    elif 200 < volume <= 300:
        tax = 100

print(f'Luggage tax: {tax:.2f}')