name = input()
games_num = int(input())
game = ''
score = 0
volley_points = 0
tennis_points = 0
badminton_points = 0
volley_in = 0
tennis_in = 0
badminton_in = 0

for i in range(games_num):
    game = input()
    score = int(input())
    if game == 'volleyball':
        volley_points += score
        volley_in += 1
    elif game == 'tennis':
        tennis_points += score
        tennis_in += 1
    elif game == 'badminton':
        badminton_points += score
        badminton_in += 1

volley_score = volley_points * 1.07
tennis_score = tennis_points * 1.05
badminton_score = badminton_points * 1.02

if (int(volley_score / volley_in) >= 75 ) and (int(tennis_score / tennis_in) >= 75) and (int(badminton_score / badminton_in) >= 75):
    print(f'Congratulations, {name}! You won the cruise games with {int(volley_score + tennis_score + badminton_score)} points.')
else:
    print(f'Sorry, {name}, you lost. Your points are only {int(volley_score + tennis_score + badminton_score)}.')