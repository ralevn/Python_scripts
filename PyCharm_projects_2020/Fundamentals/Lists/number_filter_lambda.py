## instead of conditions will use dict e.g. case

filter_commands = {
    'even': lambda number: number % 2 == 0,
    'odd': lambda number: number % 2 != 0,
    'positive': lambda number: number >= 0,
    'negative': lambda number: number < 0,
}

n = int(input())
numbers = [int(input()) for _ in range(n)]

filter_fn = filter_commands[input()]
print([n for n in numbers if filter_fn(n)])

# print(numbers, command)
# print(type(filter_fn), type(filter_commands))
