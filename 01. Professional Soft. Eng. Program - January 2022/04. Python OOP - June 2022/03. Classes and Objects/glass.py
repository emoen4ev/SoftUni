"""
4.	Glass

Create a class called Glass.

Upon initialization, it will not receive any parameters.

You must create an instance attribute called content which should be equal to 0.

You should also create a class attribute called capacity which should be 250 ml.

Create 3 instance methods:
-	fill(ml) - fills the glass with the given milliliters if there is enough space in it
and returns "Glass filled with {ml} ml", otherwise returns "Cannot add {ml} ml"
-	empty() - empties the glass and returns "Glass is now empty"
-	info() - returns info about the glass in the format "{space_left} ml left"

"""


# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if ml <= Glass.capacity - self.content:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return f'Glass is now empty'
#
#     def info(self):
#         space_left = Glass.capacity - self.content
#         return f'{space_left} ml left'


# class Glass:
#     initial_content = 0
#     capacity = 250
#
#     def __init__(self):
#         self.content = self.initial_content
#
#     def fill(self, ml):
#         if ml <= Glass.capacity - self.content:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return f'Glass is now empty'
#
#     def info(self):
#         space_left = Glass.capacity - self.content
#         return f'{space_left} ml left'


class Glass:
    initial_content = 0
    capacity = 250

    def __init__(self):
        self.content = Glass.initial_content

    def fill(self, ml):
        space_left = self.calculate_space_left()
        if space_left < ml:
            return f'Cannot add {ml} ml'

        self.content += ml
        return f'Glass filled with {ml} ml'

    def empty(self):
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        space_left = self.calculate_space_left()
        return f'{space_left} ml left'

    def calculate_space_left(self):
        return Glass.capacity - self.content


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

'''
Test Code:

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

----------------------------------------------------------------

Output:

Glass filled with 100 ml
Cannot add 200 ml
Glass is now empty
Glass filled with 200 ml
50 ml left
'''