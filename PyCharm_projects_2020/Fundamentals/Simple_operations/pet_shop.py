area = float(input())

cost = area * 7.61
discount = cost * 0.18
f_price = cost - discount

txt1 = f"The final price is: %.2f lv." %(f_price)
txt2 = f"The discount is: %.2f lv." %(discount)

print (txt1)
print(txt2)