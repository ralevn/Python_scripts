from collections import deque


def solve(people, tosses_count):
    people = deque(people)

    while people:
        people.rotate(-tosses_count + 1)
        person = people.popleft()
        if people:
            print(f'Removed {person}')
        else:
            print(f'Last is {person}')


solve(
    input().split(' '),
    int(input())
)