num_str = input()

num_1 = int(num_str[0])
num_2 = int(num_str[1])
num_3 = int(num_str[2])

for i in range(1, num_3 + 1):
    for j in range(1, num_2 + 1):
        for k in range(1, num_1 + 1):
            print(f'{i} * {j} * {k} = {k * j * i};')
