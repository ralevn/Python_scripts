animal_line = input().split(', ')

line_length = len(animal_line)

## assume word is just and list will be reversed
def find_position (li,word):
    li.reverse()
    for i in range(len(li)):
        if li[i] == word:
            return i
wolf_position = find_position(animal_line, 'wolf')

if wolf_position == 0:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!')