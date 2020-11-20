import math


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Rectangle2:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return math.pi * self.r ** 2


if __name__ == "__main__":
    rect1 = Rectangle2(5, 10, 50, 100)
    print(rect1)
