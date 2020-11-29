def number_sum(n):
    sumn = 0
    for d in n:
        sumn += int(d)
    return sumn

def find_index(i, text):
    recalc_i = i % len(text)
    return recalc_i

def remove_index(i, text):
    list_text = list(text)
    list_text.pop(i)
    return ''.join(list_text)


num_list = [n for n in input().split(' ')]
text = input()

sums = [number_sum(n) for n in num_list]

for n in sums:
    ind = find_index(n, text)
    print(text[ind], end='')
    text = remove_index(ind, text)