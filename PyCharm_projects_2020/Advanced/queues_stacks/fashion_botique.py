cloths_stack = [int(cl) for cl in input().split(' ')]
rack_capacity = int(input())
current_rack = rack_capacity

racks = 1

while cloths_stack:
    if cloths_stack[len(cloths_stack) - 1] <= current_rack:
        current_rack -= cloths_stack[len(cloths_stack) - 1]
        cloths_stack.pop()
    else:
        current_rack = rack_capacity
        racks += 1

print(racks)

