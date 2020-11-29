def characters_between (c1, c2):
    n1, n2 = ord(c1) + 1, ord(c2)
    return [chr(n) for n in range(n1, n2)]

c1 = input()
c2 = input()

for i in characters_between(c1, c2):
    print(i, end=' ')