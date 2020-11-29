a, b, c, d = int(input()), int(input()), int(input()), int(input())
## i j
## k l

for i in range(a, b+ 1):
    for j in range(a, b + 1):
        for k in range(c, d + 1):
            for l in range (c, d + 1):
                condition = (i + l == k + j) and (i != j) and (k != l)
                if condition:
                    print(f'{i}{j}')
                    print(f'{k}{l}')
                    print()
