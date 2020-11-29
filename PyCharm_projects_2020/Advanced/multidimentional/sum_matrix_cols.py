(rows, cols) = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

sum_cols = [0] * cols
print(sum_cols)

for row in range(rows):
    for col in range(cols):
        sum_cols[col] += matrix[row][col]
        # print(sum_cols)

[print(x, end=', ') for x in sum_cols]

