from project.child import Child
from project.person import Person

# child = Child('Prakash', 10)
# print(child.name)
# print(child.age)

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)

'''
Test Code:

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)

----------------------------------------------------------------

Output:

Peter
25
Person
'''