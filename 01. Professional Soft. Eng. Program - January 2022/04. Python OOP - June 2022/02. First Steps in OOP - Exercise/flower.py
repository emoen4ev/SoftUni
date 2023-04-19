"""
5.	Flower

Create a class called Flower.
Upon initialization, the class should receive a name (string) and a water_requirements (number).
The flower should also have an instance attribute called is_happy (False by default).

Add two additional methods to the class:
-	water(quantity) - it will water the flower.
Each time check if the quantity is greater than or equal to the required.
If it is - the flower becomes happy (set is_happy to True).

-	status() - it should return "{name} is happy" if the flower is happy,
otherwise it should return "{name} is not happy".

Submit only the class in the judge system.
"""


class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        self.is_happy = quantity >= self.water_requirements

    def status(self):
        # return f'{self.name} {"is" if self.is_happy else "is not"} happy'
        return f'{self.name} {("is not", "is")[self.is_happy]} happy'


flower = Flower("Lilly", 100)

flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
flower.water(10)
print(flower.status())

'''
Test Code:

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

----------------------------------------------------------------

Output:

Lilly is not happy
Lilly is not happy
Lilly is happy
'''