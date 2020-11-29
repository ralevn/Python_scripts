from collections import deque


def check_ix(queue):
    liters = 0
    distance = 0
    result = True
    for i in queue:
        liters += i[0]
        distance += i[1]
        if liters < distance:
            return False
        else:
            result = True
            liters -= distance
            distance = 0
    return result


pumps_num = int(input())

pumps = deque()


for _ in range(pumps_num):
    liters, distance_next = input().split(' ')
    pumps.append((int(liters), int(distance_next)))

start_ix = 0
result = False
while result is False:
    if check_ix(pumps):
        print(start_ix)
        result = True
    else:
        start_ix += 1
        pumps.rotate(-1)
