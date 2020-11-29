# https://softuni.bg/trainings/resources/officedocument/49803/lists-as-stacks-and-queues-lab-python-advanced-may-2020/2839
from collections import deque
queue = deque()

while True:
    command = input()
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)