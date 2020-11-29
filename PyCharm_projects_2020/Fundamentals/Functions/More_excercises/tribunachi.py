def tribunate(n):
    li = [1, 1, 2]
    for i in range(3, num):
        new_mem = li[i - 3] + li[i - 2] + li[i - 1]
        li.append(new_mem)
    return li


num = int(input())
li = [1, 1, 2]

if num >= 3:
    for i in tribunate(num):
        print(i, end=' ')
else:
    for i in range(num):
        print(li[i], end=' ')