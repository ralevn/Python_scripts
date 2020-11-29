from math import sqrt

def distance_to_center (x, y):
    distance = sqrt((x ** 2) + (y ** 2))
    return int(distance)


def find_length (x1, y1, x2, y2):
    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2)
    length = sqrt((x_diff ** 2) + (y_diff ** 2))
    return int(length)


points = [tuple([float(input()) for i in range(2)]) for j in range(4)]
#print(points)

l1 = find_length(points[0][0], points[0][1], points[1][0], points[1][1])
l2 = find_length(points[2][0], points[0][1], points[3][0], points[1][1])
d1 = distance_to_center(points[0][0], points[0][1])
d2 = distance_to_center(points[1][0], points[1][1])
d3 = distance_to_center(points[2][0], points[2][1])
d4 = distance_to_center(points[3][0], points[3][1])



if l1 >= l2:
    if d1 <= d2:
        print(f'({int(points[0][0])}, {int(points[0][1])})({int(points[1][0])}, {int(points[1][1])})', sep='')
    else:
        print(f'({int(points[1][0])}, {int(points[1][1])})({int(points[0][0])}, {int(points[0][1])})', sep='')
else:
    if d3 <= d4:
        print(f'({int(points[2][0])}, {int(points[2][1])})({int(points[3][0])}, {int(points[3][1])})', sep='')
    else:
        print(f'({int(points[3][0])}, {int(points[3][1])})({int(points[2][0])}, {int(points[2][1])})', sep='')
