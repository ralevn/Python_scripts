n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

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

def calculate_below_primary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(row + 1):
            the_sum += matrix[row][col]
    return the_sum

def calculate_below_secondary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(n - row - 1, n):
            the_sum += matrix[row][col]
    return the_sum

def calculate_above_prim_diag(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(0, n - row):
            the_sum += matrix[row][col]
    return the_sum

print('calculate_primary_diagonal_sum:  ',calculate_primary_diagonal_sum(matrix))
print('calculate_secondary_diagonal_sum:  ',calculate_secondary_diagonal_sum(matrix))
print('calculate_below_primary_diagonal_sum:  ',calculate_below_primary_diagonal_sum(matrix))
print('calculate_below_secondary_diagonal_sum:  ',calculate_below_secondary_diagonal_sum(matrix))
print('calculate_above_prim_diag:  ', calculate_above_prim_diag(matrix))