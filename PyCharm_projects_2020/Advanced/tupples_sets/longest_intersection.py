def init_sets(text):
    set1 = set()
    set2 = set()
    str1 = text.split('-')[0]
    str2 = text.split('-')[1]
    start1 = int(str1.split(',')[0])
    end1 = int(str1.split(',')[1])
    start2 = int(str2.split(',')[0])
    end2 = int(str2.split(',')[1])
    for i in range(start1, end1 + 1):
        set1.add(i)
    for i in range(start2, end2 + 1):
        set2.add(i)
    return set1, set2


def set_intersection(set1, set2):
    set_inter = set1 & set2
    return set_inter, len(set_inter)


n =int(input())

len_max = 0
max_intersection = set()
for _ in range(n):
    set1, set2 = init_sets(input())
    tmp_intersect, length = set_intersection(set1, set2)
    if length > len_max:
        len_max = length
        max_intersection = tmp_intersect

print(f'Longest intersection is {list(max_intersection)} with length {len_max}')
