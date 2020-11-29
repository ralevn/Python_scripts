"""https://softuni.bg/trainings/resources/officedocument/42863/basic-syntax-conditional-statements-and-loops-exercise-python-fundamentals-september-2019/2442"""

name = input()

while name != 'End' and name !='Johny':
    print(f'Hello, {name}!')
    name = input()

if name == 'Johnny':
    print('Hello, my love!')
else:
    print(f'Hello, {name}!')