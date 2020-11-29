n = int(input())

capacity = 255

for i in range(n):
    q = int(input())
    if capacity - q < 0:
        print('Insufficient capacity!')
    else:
        capacity -= q

print(255 - capacity)