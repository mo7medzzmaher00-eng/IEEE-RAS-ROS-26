class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s


def print_area(shape_object):
    print(shape_object.area())


c = Circle(5)
s = Square(4)

print_area(c)
print_area(s)