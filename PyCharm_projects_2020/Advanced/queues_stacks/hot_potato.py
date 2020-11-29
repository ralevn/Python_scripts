def find_right_ind(start, jump, list_n):
    ind = start + jump - 1
    if ind >= len(list_n):
        while ind >= len(list_n):
            ind -= len(list_n)
    return ind


def print_removed(ind, list_n):
    print (f'Removed {list_n.pop(ind)}')


name_list = input().split(' ')
jump = int(input())

position = 0
while len(name_list) > 1:
    ix = find_right_ind(position, jump, name_list)
    print_removed(ix, name_list)
    position = ix

print (f'Last is {name_list[0]}')