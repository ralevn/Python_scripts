days, cooks, cakes, crepes, pancakes = int(input()), int(input()), int(input()), int(input()), int(input())

cakes_sum = cakes * 45.00
crepes_sum = crepes * 5.80
pancakes_sum = pancakes * 3.20

gathered_sum = (cakes_sum + crepes_sum + pancakes_sum) * cooks * days

print (f"%.2f" % (gathered_sum - (gathered_sum * (1 /8 ))))
