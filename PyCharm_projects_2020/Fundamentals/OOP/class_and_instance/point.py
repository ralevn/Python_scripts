from math import sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x
        return new_x

    def set_y(self, new_y: int):
        self.y = new_y
        return new_y

    def distance(self, x: int, y: int):
        xd = abs(self.x - x)
        yd = abs(self.y - y)
        dist = sqrt((xd ** 2) + (yd ** 2))
        return dist


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))