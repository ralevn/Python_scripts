def first_process_string(list_str):
    if len(list_str) > 1:
        if list_str[0]+list_str[-1] in ('red', 'yellow', 'blue', 'orange', 'purple', 'green'):
            return list_str[0]+list_str[-1]
        elif list_str[-1]+string_list[0] in ('red', 'yellow', 'blue', 'orange', 'purple', 'green'):
            return list_str[-1]+string_list[0]
        else:
            return False
    else:
        if list_str[0] in ('red', 'yellow', 'blue', 'orange', 'purple', 'green'):
            return list_str[0]
        else:
            return False

def second_process_string(list_str):
    first = list_str[0][:-1]
    last = list_str[-1][:-1]
    if first:
        list_str.insert(len(list_str) // 2, first)
    if last:
        list_str.insert(len(list_str) // 2, last)
    return list_str[1:-1]


main_colors = ('red', 'yellow', 'blue')
secondary_colors = {'orange': ('red', 'yellow'),
                    'purple': ('red', 'blue'),
                    'green': ('yellow', 'blue')
                    }
string_list = input().split(' ')
found_colors = []

while string_list:
    if first_process_string(string_list):
        found_colors.append(first_process_string(string_list))
        string_list = string_list[1:-1]
    else:
        string_list = second_process_string(string_list)

for color in found_colors:
    if secondary_colors.get(color):
        if any(x not in found_colors for x in secondary_colors[color]):
            found_colors.remove(color)
            secondary_colors.pop(color)

print(found_colors)