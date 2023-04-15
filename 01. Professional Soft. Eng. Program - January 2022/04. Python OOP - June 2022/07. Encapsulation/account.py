"""
5.	Account

Create a class called Account.
Upon initialization, it should receive an id, a balance, and a pin (all numbers).
The pin and the id should be private instance attributes, and the balance should be a public attribute.
Create two public instance methods:
•	get_id(pin) - if the given pin is correct, return the id, otherwise, return "Wrong pin"
•	change_pin(old_pin, new_pin) - if the old pin is correct,
change it to the new one and return "Pin changed", otherwise return "Wrong pin"
"""


class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if self.__pin != pin:
            return 'Wrong pin'
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return 'Pin changed'
        return 'Wrong pin'


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

'''
Test Code:

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

----------------------------------------------------------------

Output:

Wrong pin
8827312
100
Wrong pin
Pin changed
'''