cards_li = input().split(' ')

team_A = set()
team_B = set()
# print(cards_li)


for card in cards_li:
    if card[0] == 'A':
        team_A.add(card)
    else:
        team_B.add(card)
    if len(team_A) > 5 or len(team_B) > 5:
        break

print(f'Team A - {11 - len(team_A)}; Team B - {11 - len(team_B)}')
# print(len(team_A), len(team_B))
if len(team_A) >= 5 or len(team_B) >= 5:
    print('Game was terminated')