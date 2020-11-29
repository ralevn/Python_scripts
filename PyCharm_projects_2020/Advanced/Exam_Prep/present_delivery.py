""" https://judge.softuni.bg/Contests/Practice/Index/2004#1 """
def locate_santa(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j
            else:
                continue


def nice_kids(matrix):
    nk = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'V':
                nk += 1
            else:
                continue
    return nk


def santa_move(direction, position, matrix):
    dirs = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
    next_row = position[0] + dirs[direction][0]
    next_col = position[1] + dirs[direction][1]
    if 0 <= position[0] < len(matrix) and 0 <= len(matrix):
        return next_row, next_col


def print_matrix(matrix, s_position):
    matrix[s_position[0]][s_position[1]] = 'S'
    for r in range(len(matrix)):
        print(*matrix[r])

presents_nu = int(input())
neighborhood_size = int(input())
neighborhood = []

for _ in range(neighborhood_size):
    neighborhood.append(input().split())

santa_pos = locate_santa(neighborhood)
nice_kids_nu = nice_kids(neighborhood)
happy_kids = 0

dir_n = input()
while dir_n != 'Christmas morning':
    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
    santa_pos = santa_move(dir_n, santa_pos, neighborhood)
    cell_v = neighborhood[santa_pos[0]][santa_pos[1]]
    if cell_v in ('-', 'X'):
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'
    elif cell_v == 'V':
        presents_nu -= 1
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'
        happy_kids += 1
        if presents_nu <= 0:
            print("Santa ran out of presents!")
            print_matrix(neighborhood, santa_pos)
            print(f'No presents for {nice_kids_nu - happy_kids} nice kid/s')
            exit()
    elif cell_v == 'C':
        r = santa_pos[0]
        c = santa_pos[1]
        for d in ((0, -1), (0, 1), (-1, 0), (+1, 0)):
            if neighborhood[r + d[0]][c + d[1]] != '-':
                presents_nu -= 1
                if neighborhood[r + d[0]][c + d[1]] == 'V':
                    happy_kids += 1
                neighborhood[r + d[0]][c + d[1]] = '-'
                if presents_nu <= 0:
                    print("Santa ran out of presents!")
                    print_matrix(neighborhood, santa_pos)
                    print(f'No presents for {nice_kids_nu - happy_kids} nice kid/s.')
                    exit()
            else:
                continue
    dir_n = input()

print_matrix(neighborhood, santa_pos)
print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
