string = input()

strength = 0
i = 0

while i < len(string):
    ch = string[i]
    if string[i] == '>':
        strength += int(string[i + 1])
    elif strength > 0:
        string_1 = string[:i]
        string_2 = string[i + 1:]
        string = string_1 + string_2
        i -= 1
        strength -= 1
    i += 1

print(string)