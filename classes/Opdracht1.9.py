class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


class Square(Rectangle):
    def set_width(self, amount):
        self.width = amount
    def set_height(self, amount):
        self.height = amount