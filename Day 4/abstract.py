from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return (22/7) * self.r * self.r
rect = Rectangle(3, 3)
circle = Circle(7)
print("Area of rectangle:", rect.area())
print("Area of circle:", circle.area())
