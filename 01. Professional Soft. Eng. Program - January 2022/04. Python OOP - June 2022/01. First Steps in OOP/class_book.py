"""
Class Book

Create a class called Book. It should have an __init__() method that should receive:
•	name: string
•	author: string
•	pages: int

Submit only the class in the judge system.
"""


class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.name}" by {self.author} has {self.pages}'


'''
Test Code:

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

----------------------------------------------------------------

Output:

My Book
Me
200
'''

# b = Book('Harry Potter and GoF', 'J.K.Rowling', 500)
#
# print(b)
# print(str(b))
# print(b.name)
# print(b.author)
# print(b.pages)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name} is the best animal ...'
#
#     def sleep(self):
#         return "sleeping .."
#
# animal = Animal("cat")
# print(animal.sleep())
# print(animal.name)
# print(animal)