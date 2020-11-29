event = ''
coffee = 0

while event != 'END':
    event = input()
    if event in ['dog', 'cat', 'movie', 'coding']:
        coffee += 1
    elif event in ['DOG', 'CAT', 'MOVIE', 'CODING']:
        coffee += 2
    else:
        continue

if coffee <= 5:
    print(coffee)
else:
    print('You need extra sleep')
