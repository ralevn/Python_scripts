needed_experience = int(input())
battles = int(input())
current_experience = 0


for battle in range(1, battles + 1):
    gained_experience = int(input())
    if battle % 3 == 0:
        current_experience += gained_experience * 1.15
    if battle % 5 == 0:
        current_experience += gained_experience * 0.90
    if battle % 3 != 0 and battle % 5 != 0:
        current_experience += gained_experience
    if current_experience >= needed_experience:
        print (f'Player successfully collected his needed experience for {battle} battles.')
        break

if current_experience < needed_experience:
    print(f'Player was not able to collect the needed experience, '
          f'{needed_experience - current_experience:.2f} more needed.')

