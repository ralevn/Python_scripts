n, m = [int(x) for x in input().split()]
text = input()

count = 0

matrix = [['' for _ in range(m)] for _ in range(n)]

for row in range(n):
    if row % 2 != 0:
        for col in range(m - 1, -1, -1):
            matrix[row][col] = text[count]
            count += 1
            if count > len(text) - 1:
                count = 0
    else:
        for col in range(m):
            matrix[row][col] = text[count]
            count += 1
            if count > len(text) -1 :
                count = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end='')
    print()