n, m = [int(x) for x in input().split()]
text = input()

count = 0
matrix = []

for row in range(n):
    matrix.append([])
    for col in range(m):
        matrix[row].append(count)
        count += 1

print(*matrix, sep='\n')