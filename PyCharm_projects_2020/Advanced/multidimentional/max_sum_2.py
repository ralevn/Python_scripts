(rows, cols) = [int(n) for n in input().split(' ')]

matrix = []
for _ in range(rows):
    row = [int(n) for n in input().split(' ')]
    matrix.append(row)

max_matrix = []
max_sum = -9999999999

for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = []
        current_sum = 0
        row_count = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_count].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = sub_matrix

print(f'Sum = {max_sum}')
for row in max_matrix:
    print(' '.join([str(x) for x in row]))