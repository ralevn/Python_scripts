numbers = [int(n) for n in input().split(', ')]
beggers = int(input())

result = [0] * beggers
i = 0

while len(numbers) > 0:
    for j in range(beggers):
        if len(numbers) == 0:
            break
        else:
            result[j] += numbers.pop(i)

print(result)
