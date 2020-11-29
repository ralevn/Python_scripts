guests_count = int(input())
presents_count = int(input())

money = electrics = vauchers = others = 0

for i in range(presents_count):
    present_type = input()
    if present_type== 'A': money += 1
    elif present_type == 'B': electrics += 1
    elif present_type == 'V': vauchers += 1
    elif present_type == 'G': others += 1

money_per = (money / presents_count) * 100
electrics_per = (electrics / presents_count) * 100
vauchers_per = (vauchers / presents_count) * 100
others_per = (others / presents_count) * 100
present_per = (presents_count / guests_count) * 100

print(f'{money_per:.2f}%')
print(f'{electrics_per:.2f}%')
print(f'{vauchers_per:.2f}%')
print(f'{others_per:.2f}%')
print(f'{present_per:.2f}%')