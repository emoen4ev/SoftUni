# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if ml <= self.capacity - self.content:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return f'Glass is now empty'
#
#     def info(self):
#         space_left = self.capacity - self.content
#         return f'{space_left} ml left'


# class Glass:
#     initial_content = 0
#     capacity = 250
#
#     def __init__(self):
#         self.content = self.initial_content
#
#     def fill(self, ml):
#         if ml <= self.capacity - self.content:
#             self.content += ml
#             return f'Glass filled with {ml} ml'
#         return f'Cannot add {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return f'Glass is now empty'
#
#     def info(self):
#         space_left = self.capacity - self.content
#         return f'{space_left} ml left'


class Glass:
    initial_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.initial_content

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
        return self.capacity - self.content


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())