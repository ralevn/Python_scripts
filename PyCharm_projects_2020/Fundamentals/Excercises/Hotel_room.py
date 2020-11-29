month = input()
nights = int(input())

discount_st = 1
if nights > 14:
    discount_appt = 0.90
else:
    discount_appt = 1

if month in ['May', 'October']:
    studio_price = 50
    appt_price = 65
    if nights > 7:
        discount_st = 0.95
    if nights > 14:
        discount_st = 0.70
elif month in ['June', 'September']:
    studio_price = 75.20
    appt_price = 68.70
    if nights > 14:
        discount_st = 0.80
elif month in ['July', 'August']:
    studio_price = 76
    appt_price = 77

print(f'Apartment: {appt_price * nights * discount_appt:.2f} lv.')
print(f'Studio: {studio_price * nights * discount_st :.2f} lv.')