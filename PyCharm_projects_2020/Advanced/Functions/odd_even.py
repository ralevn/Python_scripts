def even_odd_sum(cmd, listn):
    if cmd == 'Odd':
        result = sum([i for i in listn if i % 2 != 0])
    elif cmd == 'Even':
        result = sum([i for i in listn if i % 2 == 0])
    return result


command = input()
listn = [int(i) for i in input().split(' ')]

list_len = len(listn)
print(even_odd_sum(command, listn) * list_len)