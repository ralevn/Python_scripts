n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split(' '))

diag_sum = 0
for i in range(len(matrix)):
    diag_sum += int(matrix[i][i])

print(diag_sum)