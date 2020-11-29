def find_snake(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'S':
                return r, c

def find_burrows(matrix):
    list_b = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                list_b.append((r, c))
    return list_b

def snake_move(dir_n, pos, matrix):
    dirs = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
    matrix[pos[0]][pos[1]] = '.'
    next_row = pos[0] + dirs[dir_n][0]
    next_col = pos[1] + dirs[dir_n][1]
    return next_row, next_col

n = int(input())

territory = []
for _ in range(n):
    row = [x for x in list(input())]
    territory.append(row)


s_pos = find_snake(territory)
eaten_f = 0
burrows = find_burrows(territory)


while True:
    dir_n = input()
    s_pos = snake_move(dir_n, s_pos, territory)
    r = s_pos[0]
    c = s_pos[1]
    if (r >= n or r < 0) or (c >= n or c < 0):
        game_over = True
        print('Game over!')
        break
    elif s_pos in burrows:
        burrows.remove(s_pos)
        s_pos = burrows[0]
        for p in find_burrows(territory):
            territory[p[0]][p[1]] = '.'
    elif territory[r][c] == '*':
        eaten_f += 1
        if eaten_f == 10:
            print('You won! You fed the snake.')
            territory[s_pos[0]][s_pos[1]] = 'S'
            break

print(f"Food eaten: {eaten_f}")
for row in territory:
    print(''.join(row))
