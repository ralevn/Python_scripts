def validate(string):
    is_valid = True
    boss = ''
    title = ''

    if ':' not in string:
        is_valid = False
    elif string.count('|') != 2:
        is_valid = False
    elif string.count('#') != 2:
        is_valid = False

    str_1 = string.split(':')[0]
    str_2 = string.split(':')[1]
    if str_1[0] != '|' or str_1[len(str_1) - 1] != '|':
        is_valid = False
    elif str_2[0] != '#' or str_2[len(str_2) - 1] != '#':
        is_valid = False
    else:
        boss = str_1[1:-1]
        title = str_2[1:-1]

    if not boss.isupper():
        is_valid = False
    elif not boss.isalpha():
        is_valid = False
    elif len(boss) < 4:
        is_valid = False
    elif title.count(' ') != 1:
        is_valid = False
    elif not title.split(' ')[0].isalpha() or not title.split(' ')[1].isalpha() :
        is_valid = False

    if is_valid:
        print(f'{boss}, The {title}')
        print(f'>> Strength: {len(boss)}')
        print(f'>> Armour: {len(title)}')
    else:
        print('Access denied!')


n = int(input())

for i in range(n):
    string = input()
    validate(string)



