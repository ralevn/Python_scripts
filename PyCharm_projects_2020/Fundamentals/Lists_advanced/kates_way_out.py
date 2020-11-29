def find_position(s, matrix):
    position = [[r, c] for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == s]
    return position


def find_exit(matrix):
    exit_p = [[r, c] for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == ' ' and
            (r == 0 or c == 0 or r == len(matrix) - 1 or c == len(matrix[r]) - 1)]
    return exit_p


def check_neighbour_indices(r, c, matrix):
    up = []
    right = []
    down = []
    left = []
    if r == 0: up = None
    elif r == len(matrix): down = None
    else:
        up.append(r - 1)
        up.append(c)
        down.append(r + 1)
        down.append(c)
    if c == 0: left = None
    elif c == len(matrix[r]): right = None
    else:
        right.append(r)
        right.append(c + 1)
        left.append(r)
        left.append(c - 1)
    return matrix[up[0]][up[1]], matrix[right[0]][right[1]], matrix[down[0]][down[1]], matrix[left[0]][left[1]]


n = int(input())

maze = [list(input()) for i in range(n)]
print([i for i in maze])
print(*find_position('k', maze))
print(*find_position(' ', maze))
print(*find_exit(maze))

print(check_neighbour_indices(0, 4, maze))