def sum_ascii(text):
    ascii_sum = 0
    for i in text:
        ascii_sum += ord(i)
    return ascii_sum


n = int(input())

even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    value = sum_ascii(name) // i
    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    print(', '.join([str(x) for x in odd_set.union(even_set)]))
elif odd_sum > even_sum:
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))