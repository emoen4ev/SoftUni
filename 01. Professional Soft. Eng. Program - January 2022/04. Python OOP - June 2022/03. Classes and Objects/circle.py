"""
3.	Circle

Create a class called Circle.
Upon initialization, it should receive a radius (number).
Create a class attribute called pi which should be equal to 3.14.
Create 3 instance methods:
-	set_radius(new_radius) - changes the radius
-	get_area() - returns the area of the circle
-	get_circumference() - returns the circumference of the circle

"""


class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int):
        self.radius = new_radius

    def get_area(self):
        area = Circle.pi * self.radius ** 2
        return area

    def get_circumference(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

'''
Test Code:

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

----------------------------------------------------------------

Output:

452.16
75.36
'''