"""
4.	Shapes

Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter.
Create classes Circle (receives radius upon initialization)
and Rectangle (receives height and width upon initialization) that implement those methods (returning the result).
The fields of Circle and Rectangle should be private.

Submit all the classes and your imports in the judge system
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    # def __init__(self):
    #     pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        # super().__init__()
        self.__radius = r

    def calculate_area(self):
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, h, w):
        # super().__init__()
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

'''
Test Code:

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

----------------------------------------------------------------

Output:

78.53981633974483
31.41592653589793
200
60
'''