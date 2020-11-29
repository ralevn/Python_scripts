n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diag = [matrix[i][i] for i in range(n)]
secondary_diag = [matrix[i][-i -1] for i in range(n)]

print(f'First diagonal: {", ".join(str(x) for x in primary_diag)}. Sum: {sum(primary_diag)}')
print(f'Second diagonal: {", ".join(str(x) for x in secondary_diag)}. Sum: {sum(secondary_diag)}')