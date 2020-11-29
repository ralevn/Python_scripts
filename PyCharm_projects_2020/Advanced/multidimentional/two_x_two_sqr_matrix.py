def check_submatrix(matrix, row, col):
    answer = True
    ch = matrix[row][col]
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            if matrix[r][c] == ch:
                continue
            else:
                return False
    return answer


(rows, cols) = [int(n) for n in input().split(' ')]

matrix = []
for _ in range(rows):
    row = [n for n in input().split(' ')]
    matrix.append(row)

count = 0
for row in range(rows -2 + 1):
    for col in range(cols - 2 + 1):
        if check_submatrix(matrix, row, col):
            count += 1

print(count)
