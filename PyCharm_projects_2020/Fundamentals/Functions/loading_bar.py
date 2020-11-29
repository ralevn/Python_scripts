def visualizer (n):
    list_v = ['.'] * 10
    tn = n // 10
    string = ''
    for i in range(tn):
        list_v[i] = '%'
    for ch in list_v:
        string += ch
    return '[' + string + ']'

status = int(input())

if status == 100:
    print(f'100% Complete!\n{visualizer(status)}')
else:
    print(f'{status}% {visualizer(status)}\nStill loading...')

