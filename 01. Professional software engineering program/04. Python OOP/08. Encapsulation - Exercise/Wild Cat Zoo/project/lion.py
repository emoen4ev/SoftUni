from .animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        money_for_care = self.MONEY_FOR_CARE
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)