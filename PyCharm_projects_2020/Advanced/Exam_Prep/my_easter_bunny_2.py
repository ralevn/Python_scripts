def find_bunny_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                return i, j
            else:
                continue


field_size = int(input())
field = [input().split() for i in range(field_size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

eggs_collected = {
    'left': 0,
    'right': 0,
    'up': 0,
    'down': 0
}

eggs_positions = {
    'left': [],
    'right': [],
    'up': [],
    'down': []
}

bunny_position = find_bunny_pos(field)

for dir_b in directions:
    r_offset = directions[dir_b][0]
    c_offset = directions[dir_b][1]
    current_position = [bunny_position[0] + r_offset, bunny_position[1] + c_offset]
    while all(0 <= i < len(field) for i in current_position):
        if field[current_position[0]][current_position[1]] != 'X':
            eggs_collected[dir_b] += int(field[current_position[0]][current_position[1]])
            eggs_positions[dir_b].append(current_position)
            current_position = [current_position[0] + r_offset, current_position[1] + c_offset]
        else:
            break

max_dir = max(eggs_collected, key=eggs_collected.get)
print(max_dir)
print(*eggs_positions[max_dir], sep='\n')
print(eggs_collected[max_dir])
