year_type = input()
holydays_count = int(input())
travel_count = int(input())

we_sofia = (48 - travel_count) * (3 / 4)
holidays_sofia = holydays_count * (2 / 3)

games = we_sofia + travel_count + holidays_sofia

if year_type == 'leap':
    games = games * 1.15

print(int(games))


