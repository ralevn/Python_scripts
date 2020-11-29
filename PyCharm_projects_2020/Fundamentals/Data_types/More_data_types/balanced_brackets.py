n = int(input()) # number of lines

opened_num = 0
closed_num = 0
balanced = 'UNBALANCED'
string_list = []

for i in range(n):
    line = input()
    string_list.append(line)

for i in range(len(string_list)):
    if string_list[i] == '(':
        if string_list[i - 1] =='(':
            balanced = 'UNBALANCED'
            break
        opened_num += 1
    if string_list[i] == ')':
        closed_num += 1
        if opened_num == closed_num:
            balanced = 'BALANCED'

## print(string_list)
print(balanced)