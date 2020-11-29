def find_bunny_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                return i, j
            else:
                continue


def move_up(row, col, matrix):
    if row == 0:
        return False
    else:
        sum_u = 0
        for r in range(row - 1, -1, -1):
            if matrix[r][col] != 'X':
                sum_u += int(matrix[r][col])
            else:
                break
    return sum_u


def move_down(row, col, matrix):
    if row == len(matrix) - 1:
        return False
    else:
        sum_d = 0
        for r in range(row + 1, len(matrix)):
            if matrix[r][col] != 'X':

                sum_d += int(matrix[r][col])
            else:
                break
    return sum_d


def move_right(row, col, matrix):
    if col == len(matrix[row]) -1:
        return False
    else:
        sum_r = 0
        for c in range(col + 1, len(matrix[row])):
            if matrix[row][c] != 'X':
                sum_r += int(matrix[row][c])
            else:
                break
    return sum_r


def move_left(row, col, matrix):
    if col == 0:
        return False
    else:
        sum_l = 0
        for c in range(col - 1, -1, -1):
            if matrix[row][c] != 'X':
                sum_l += int(matrix[row][c])
            else:
                break
    return sum_l


field_size = int(input())
field = [input().split(' ') for i in range(field_size)]

eggs_number = 0
bunny_row = find_bunny_pos(field)[0]
bunny_col = find_bunny_pos(field)[1]

max_eggs = 0

print(move_up(bunny_row, bunny_col, field))
print(move_right(bunny_row, bunny_col, field))
print((move_down(bunny_row, bunny_col, field)))
print(move_left(bunny_row, bunny_col, field))

print(*field, sep='\n')
print(find_bunny_pos(field))
