def get_submatrix_sum(matrix, row, col):
    the_sum = 0
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            the_sum += matrix[r][c]
    return the_sum


def print_summatrix(matrix, row, col):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            print(matrix[r][c], end=' ')
        print()


(rows, cols) = [int(n) for n in input().split()]

matrix = []
for _ in range(rows):
    row = [int(n) for n in input().split()]
    matrix.append(row)

max_position = (0, 0)
max_sum = get_submatrix_sum(matrix, 0, 0)

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = get_submatrix_sum(matrix, row, col)
        if current_sum > max_sum:
            max_sum = current_sum
            max_position = (row, col)

max_row, max_col = (max_position)

print(f'Sum = {max_sum}')
print_summatrix(matrix, max_row, max_col)
