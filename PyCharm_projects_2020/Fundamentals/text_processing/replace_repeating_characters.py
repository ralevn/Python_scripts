string = list(input())
new_string = []

for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        new_string.append(string[i])

new_string.append(string[-1])

print(''.join(new_string))