from project.meals.meal import Meal


class FoodOrdersApp:
    added_meals = []

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        pass

    def add_meals_to_menu(self, *meals: Meal):
        pass

    def show_menu(self):
        pass

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        pass

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        return f'Food Orders App has {len(self.added_meals)} meals on the menu and {len(self.clients_list)} clients.'