strange_zoo = []

for _ in range(3):
    strange_zoo.append(input())

print(strange_zoo)
print(strange_zoo[::-1])
normal_zoo = reversed(strange_zoo)
print(normal_zoo)

for i in normal_zoo:
    print(i)
print(type(normal_zoo))
nl = list(normal_zoo)
print(nl)