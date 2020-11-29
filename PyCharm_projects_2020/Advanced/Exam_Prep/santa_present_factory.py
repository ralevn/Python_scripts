""" https://judge.softuni.bg/Contests/Practice/Index/2004#0 """
from collections import deque


def process_cycle(materials, magics, toys):
    if materials and magics:
        mat = materials[-1]
        mag = magics[0]
        if mat == 0 and mag == 0:
            materials.pop()
            magics.popleft()
            return False
        if mag == 0:
            magics.popleft()
            return False
        if mat == 0:
            materials.pop()
            return False
        if mat * mag < 0:
            materials.pop()
            magics.popleft()
            materials.append(mat + mag)
        elif mat * mag in toys:
            materials.pop()
            magics.popleft()
            return toys[mat * mag]
        elif mat * mag not in toys:
            magics.popleft()
            materials[-1] += 15
    else:
        return False


present_names = ('Doll', 'Wooden train', 'Teddy bear', 'Bicycle')
needed_magic = (150, 250, 300, 400)
presents = dict(zip(needed_magic, present_names))


boxes = [int(n) for n in input().split()]
magic = deque(int(n) for n in input().split())
crafted_toys = []

while boxes and magic:
    result = process_cycle(boxes, magic, presents)
    if result:
        crafted_toys.append(result)
    else:
        continue

if (present_names[0] in crafted_toys and present_names[1] in crafted_toys) or \
(present_names[2] in crafted_toys and present_names[3] in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
    job_done = True
else:
    print('No presents this Christmas!')

if boxes:
    boxes = boxes[::-1]
    print(f"Materials left: {', '.join(str(n) for n in boxes)}")
if magic:
    print(f"Magic left: {', '.join(str(n) for n in magic)}")

for p in sorted(set(crafted_toys)):
    print(f'{p}: {crafted_toys.count(p)}')