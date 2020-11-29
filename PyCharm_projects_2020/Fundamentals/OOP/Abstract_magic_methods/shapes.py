from math import pi

class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass

    def print_shape_info(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return f'{2 * pi * self.radius:.2f}'

    def area(self):
        return f'{pi * (self.radius ** 2):.2f}'

    def print_shape_info(self):
        text = f'radius: {self.radius}, perimeter: {self.perimeter()}: area: {self.area()}'
        return text

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.height * self.width

    def print_shape_info(self):
        text = f'width: {self.width}, height: {self.height}, perimeter: {self.perimeter()}: area: {self.area()}'
        return text


circle1 = Circle(3)
circle2 = Circle(4)
rectangle1 = Rectangle(2, 5)
rectangle2 = Rectangle(3,4)


shapes = [circle1, circle2, rectangle1, rectangle2]

for f in shapes:
    #print(f.area(), f.perimeter())
    print(f.print_shape_info())