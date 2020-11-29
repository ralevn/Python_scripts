def get_command_input(text):
    list_c = text.split('->')
    if list_c[0] == 'END':
        command = [list_c[0]]
        return command
    elif list_c[0] == 'Add':
        command = list_c[0]
        store = list_c[1]
        item_list = list_c[2].split(',')
        return command, store, item_list
    elif list_c[0] == 'Remove':
        command = list_c[0]
        store = list_c[1]
        return command, store


def sort_list(li):
    return sorted(li, key=li.count, reverse=True)


def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda i: (len(i[1]), i[0]), reverse=True))


command = get_command_input(input())
list_of_items = {}

while command[0] != 'END':
    operation = command[0]
    store = command[1]
    if operation == 'Add':
        items = command[2]
        if store not in list_of_items:
            list_of_items[store] = []
        for item in items:
            list_of_items[store].append(item)
    if operation == 'Remove':
        if store in list_of_items:
            for i in list_of_items:
                for j in list_of_items[store]:
                    if j in list_of_items[i]:
                        list_of_items[i].remove(j)
            del list_of_items[store]
    command = get_command_input(input())


list_of_items = sort_dict(list_of_items)

print('Stores list:')
for i in list_of_items:
    print(i)
    for j in list_of_items[i]:
        print(f'<<{j}>>')
