def calculate_primary_diagonal_sum(matrix):
    primary_diagonal_sum = 0
    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


def calculate_secondary_diagonal_sum(matrix):
    secondary_diagonal_sum = 0
    n = len(matrix)
    for i in range(n):
        secondary_diagonal_sum += matrix[i][- i - 1]
    return secondary_diagonal_sum


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

print(abs(calculate_primary_diagonal_sum(matrix) - calculate_secondary_diagonal_sum(matrix)))