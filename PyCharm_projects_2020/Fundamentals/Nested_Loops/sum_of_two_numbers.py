"""
Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от
две дадени числа. На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен
на дадено магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение,
че не е намерено.
Входът се чете от конзолата и се състои от три реда:
⦁	Първи ред – начало на интервала – цяло число в интервала [1...999]
⦁	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
⦁	Трети ред – магическото число – цяло число в интервала [1...10000]
"""

begin_num = int(input())
end_num = int(input())
magic_number= int(input())

counter = 0
hits = 0
condition = (magic_number > end_num * 2) or (magic_number < begin_num)

for i in range(begin_num, end_num + 1):
    for j in range(begin_num, end_num + 1):
        counter += 1
        if  hits != 1:  ### така ще избегнем излишни проверки защото искат само първия hit
            if i + j == magic_number:
                hits += 1
                print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
            else:
                continue
        else:
            continue
if hits == 0 :
    print(f'{counter} combinations - neither equals {magic_number}')
