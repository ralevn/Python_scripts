words = [word.lower() for word in input().split(' ')]

odds ={}

for word in words:
    if word not in odds:
        odds[word] = 0
    odds[word] += 1

for (k, v) in odds.items():
    if v % 2 != 0:
        print(k, end=' ')
