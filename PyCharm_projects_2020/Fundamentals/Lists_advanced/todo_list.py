task = input().split('-', maxsplit=1)

task_list = {}

while task[0] != 'End':
    task_list[int(task[0])] = task[1]
    task = input().split('-', maxsplit=1)

print([v for i, v in sorted(task_list.items())])