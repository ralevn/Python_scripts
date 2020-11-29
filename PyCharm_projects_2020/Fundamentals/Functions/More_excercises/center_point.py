from math import sqrt

def find_distance (x, y):
    distance = sqrt(abs((x ** 2) + (y ** 2)))
    return int(distance)

points = [tuple([float(input()) for i in range(2)]) for j in range(2)]

d1 = find_distance(points[0][0], points[0][1])
d2 = find_distance(points[1][0], points[1][1])


if d1 <= d2:
    print(points[0])
else:
    print(points[1])
