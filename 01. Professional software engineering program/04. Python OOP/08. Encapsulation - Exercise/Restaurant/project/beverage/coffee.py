from Restaurant.project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, price, milliliters, caffeine: float):
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine
        self.MILLILITERS = milliliters
        self.PRICE = price

    @property
    def caffeine(self):
        return  self.__caffeine