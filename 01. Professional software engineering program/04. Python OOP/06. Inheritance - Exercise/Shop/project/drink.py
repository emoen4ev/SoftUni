from .product import Product


class Drink(Product):
    def __init__(self, name: str, quantity: int):
        super().__init__(name, quantity=10)