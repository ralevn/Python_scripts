line_numb = int(input())
stack = []

for _ in range(line_numb):
    line = input().split()
    if line[0] == '1':
        entry = int(line[1])
        stack.append(entry)
    elif line[0] == '2':
        if stack:
            stack.pop()
    elif line[0] == '3':
        if stack:
            print(max(stack))
    elif line[0] == '4':
        if stack:
            print(min(stack))

# print(*stack, sep=', ')

print(', '.join(map(str, reversed(stack))))