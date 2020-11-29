numbers = [int(n) for n in input().split(' ')]
mins = int(input())

for _ in range(mins):
    smallest = min(numbers)
    numbers.remove(smallest)

print(numbers)