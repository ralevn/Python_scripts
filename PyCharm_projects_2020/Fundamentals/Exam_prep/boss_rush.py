import re
num = int(input())

boss_pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#'


for _ in range(num):
    string = input()
    if re.search(boss_pattern, string):
        boss = re.match(boss_pattern,string).group(1)
        title = re.match(boss_pattern,string).group(2)
        if boss and title:
            print(f'{boss}, The {title}')
            print(f'>> Strength: {len(boss)}')
            print(f'>> Armour: {len(title)}')
    else:
        print('Access denied!')