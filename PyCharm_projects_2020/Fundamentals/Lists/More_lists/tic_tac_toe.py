field = [[int(element) for element in input().split(' ')] for rows in range(3)]
zipped = list(zip(*field)) ## *field unpacks list to its elements i.e inner lists which we then zip
is_first = False
is_second = False

#for row in field:
#    print(' '.join([str(element) for element in row]))

#for row in zipped:
#    print(' '.join([str(element) for element in row]))

## check rows:
for i in range(3):
    if field[i].count(1) == 3:
        is_first = True
        break
    elif field[i].count(2) == 3:
        is_second = True
        break
## check columns:
    elif zipped[i].count(1) == 3:
        is_first = True
        break
    elif zipped[i].count(2) == 3:
        is_second = True
        break

## check main diagonal:
if [field[i][i] for i in range(3)].count(1) == 3:
    is_first = True
elif [field[i][i] for i in range(3)].count(2) == 3:
    is_second = True

## check secondary diagonal:
if [field[i][2 - i] for i in range(3)].count(1) == 3:
    is_first = True
elif [field[i][2 - i] for i in range(3)].count(2) == 3:
    is_second = True

if is_first == True:
    print('First player won')
elif is_second == True:
    print('Second player won')
else:
    print('Draw!')