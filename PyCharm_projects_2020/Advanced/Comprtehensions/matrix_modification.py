def read_matrix():
    rows_count = int(input())
    return [[int(x)
            for x in input().split()]
            for _ in range(rows_count)]


matrix = read_matrix()

line = input()
while line != 'END':
    command = line.split(' ')[0]
    row, col, val = (int(line.split(' ')[1])), (int(line.split(' ')[2])), (int(line.split(' ')[3]))
    if row < 0 or row >= len(matrix):
        print('Invalid coordinates')
    elif col < 0 or col >= len(matrix[row]):
        print('Invalid coordinates')
    elif command == 'Add':
        matrix[row][col] += val
    elif command == 'Subtract':
        matrix[row][col] -= val
    line = input()

for r in matrix:
    print(*r)