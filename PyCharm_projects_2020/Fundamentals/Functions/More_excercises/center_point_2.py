def find_closest(x1, y1, x2, y2):
    result1 = abs(x1) + abs(y1)
    result2 = abs(x2) + abs(y2)
    if result1 <= result2:
        print(f'({int(x1)}, {int(y1)})')
    else:
        print(f'({int(x2)}, {int(y2)})')


p = [[float(input()) for i in range(2)] for j in range(2)]

find_closest(p[0][0], p[0][1], p[1][0], p[1][1])