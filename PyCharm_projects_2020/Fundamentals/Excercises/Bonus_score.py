number = int(input())
bonus1, bonus2, bonus3 = 0, 0, 0

if number <= 100:
    bonus1 = 5
elif 100 < number <= 1000:
    bonus1 = number * 0.2
else:
    bonus1 = number * 0.1

if number % 2 == 0: bonus2 = 1
if (number % 2 != 0 and number % 5 == 0): bonus3 = 2

print (bonus1 + bonus2 + bonus3)
print (number + bonus1 + bonus2 + bonus3)