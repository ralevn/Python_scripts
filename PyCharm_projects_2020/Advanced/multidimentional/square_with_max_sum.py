def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]

def get_submatrix_sum(matrix, row, col):
    the_sum = 0
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            the_sum += matrix[r][c]
    return the_sum


def print_summatrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=' ')
        print()


(rows, cols) = read_int_list_from_input(', ')
matrix = [read_int_list_from_input(', ') for _ in range(rows)]

max_position = (0, 0)
max_sum = 0

for row in range(rows -2 + 1):
    for col in range(cols - 2 + 1):
        current_sum = get_submatrix_sum(matrix, row, col)
        if current_sum > max_sum:
            max_sum = current_sum
            max_position = (row, col)

max_row, max_col = (max_position)
print_summatrix(matrix, max_row, max_col)
print(max_sum)