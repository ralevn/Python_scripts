def check_validity(line, row, col):
    answer = True
    line_tup = tuple(x for x in line.split())
    if len(line_tup) != 5:
        answer = False
        return answer
    elif line_tup[0] != 'swap':
        answer = False
        return answer
    elif int(line_tup[1]) > row \
            or int(line_tup[2]) > row \
            or int(line_tup[3]) > col \
            or int(line_tup[4]) > col:
        answer = False
        return answer
    return answer

def process_line(line):
    row1 = int(line.split()[1])
    col1 = int(line.split()[2])
    row2 = int(line.split()[3])
    col2 = int(line.split()[4])
    return row1, col1, row2, col2

def swap_matrix_elements(matrix, row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def print_matrix(matrix):
    for r in range(len(matrix)):
        print(*matrix[r])

rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    row = [x for x in input().split()]
    matrix.append(row)

line = input()
while line != 'END':
    if check_validity(line, rows, cols):
        row1, col1, row2, col2 = process_line(line)
        matrix = swap_matrix_elements(matrix, row1, col1, row2, col2)
        print_matrix(matrix)
    else:
        print('Invalid input!')
    line = input()