n = int(input())

uniques = set()

for _ in range(n):
    for el in input().split(' '):
        uniques.add(el)

print(*uniques, sep='\n')