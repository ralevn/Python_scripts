def valid_position(position, size):
    row, col = position[0], position[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knights = 0
    row_offset = [-2, -1, 1, 2, 2, 1, -1, -2]
    col_offset = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        position = [row + row_offset[i], col + col_offset[i]]
        if valid_position(position, size) and board[position[0]][position[1]] == 'K':
            killed_knights += 1
    return killed_knights


n = int(input())

total_kills = 0
board = []
for _ in range(n):
    board.append([x for x in input()])

while True:
    max_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > max_kills:
                    max_kills = killed_knights
                    to_kill = [row, col]

    if max_kills == 0:
        break

    to_kill_r = to_kill[0]
    to_kill_c = to_kill[1]
    board[to_kill_r][to_kill_c] = '0'
    total_kills += 1

print(total_kills)
