def richest(list_p):
    return list_p.index(max(list_p))


def poorest(list_p):
    return list_p.index(min(list_p))


def distribute(n, list_p):
    while list_p[poorest(list_p)] < n:
        list_p[poorest(list_p)] += 1
        list_p[richest(list_p)] -= 1
    return list_p


population = [int(p) for p in input().split(', ')]
min_wealth = int(input())

is_possible = True

if sum(population) < min_wealth * len(population):
    is_possible = False
else:
    population = distribute(min_wealth, population)

if is_possible:
    print(population)
else:
    print('No equal distribution possible')