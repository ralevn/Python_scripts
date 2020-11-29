string_numbs = [int(n) for n in input().split(', ')]

print([i for i, v in enumerate(string_numbs) if v % 2 == 0])