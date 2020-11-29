n = int(input())
uniqs = set()

for _ in range(n):
    uniqs.add(input())

print(*uniqs, sep='\n')