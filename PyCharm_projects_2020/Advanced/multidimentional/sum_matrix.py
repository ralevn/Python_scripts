(rows, cols) = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(',')]
    matrix.append(row)

sum_matrix = 0
for row in matrix:
    sum_matrix += sum(row)

print(sum_matrix)
print(matrix)