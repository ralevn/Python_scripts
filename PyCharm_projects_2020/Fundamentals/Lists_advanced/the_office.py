def average (li):
    return sum(li) / len(li)


employee_happiness = [int(n) for n in input().split(' ')]
happiness_factor = int(input())

factored_happiness = [n * happiness_factor for n in employee_happiness]
happy_employees = len([emp for emp in factored_happiness if emp >= average(factored_happiness)])

text1 = f'Score: {happy_employees}/{len(employee_happiness)}. '

if happy_employees >= len(employee_happiness) / 2:
    text2 = 'Employees are happy!'
else:
    text2 = 'Employees are not happy!'

print(text1 + text2)