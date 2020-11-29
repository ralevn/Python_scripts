veg_price, fruit_price = float(input()) / 1.94, float(input()) / 1.94
veg_kg, frui_kg = int(input()), int(input())

# print(veg_price, veg_kg, fruit_price, frui_kg)

profit = (veg_price * veg_kg) + (fruit_price * frui_kg)

print(f'%.2f' %(profit))

