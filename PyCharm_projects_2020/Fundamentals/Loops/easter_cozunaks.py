budget = float(input())
flour_price = float(input())

pack_egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
milk_cost = milk_price * 0.25

cozunak_cost = pack_egg_price + flour_price + milk_cost
cozunak_number = 0
color_egg_numb  = 0

while budget >= cozunak_cost:
    budget -= cozunak_cost
    if budget >= 0:
        cozunak_number += 1
        if cozunak_number % 3 != 0:
            color_egg_numb += 3
        else:
            color_egg_numb += 3
            color_egg_numb -= (cozunak_number - 2)

print(f'You made {cozunak_number} cozonacs! Now you have {color_egg_numb} eggs and {budget:.2f}BGN left.')