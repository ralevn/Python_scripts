from collections import deque


def add_second(time_txt):
    h = int(time_txt.split(':')[0])
    m = int(time_txt.split(':')[1])
    s = int(time_txt.split(':')[2])
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return f'{h:02d}:{m:02d}:{s:02d}'


robots = {}
free_robots = deque()
busy_robots = []
products_queue = deque()


for item in input().split(';'):
    name, operate = item.split('-')[0], int(item.split('-')[1])
    robots[name] = operate
    free_robots.append(name)
time = input()
robots_specifications = robots.copy()

product = input()
while product != 'End':
    products_queue.appendleft(product)
    product = input()

while products_queue:
    if free_robots:
        product = products_queue.pop()
        robot = free_robots.popleft()
        busy_robots.append(robot)
        time = add_second(time)
        print(f'{robot} - {product} [{time}]')
        for r in busy_robots:
            robots[r] -= 1
            if robots[r] == 0:
                free_robots.append(r)
                busy_robots.remove(r)
                robots[r] = robots_specifications[r]
    else:
        products_queue.rotate(1)
        for r in busy_robots:
            robots[r] -= 1
            if robots[r] == 0:
                free_robots.append(r)
                busy_robots.remove(r)
                robots[r] = robots_specifications[r]
        time = add_second(time)
