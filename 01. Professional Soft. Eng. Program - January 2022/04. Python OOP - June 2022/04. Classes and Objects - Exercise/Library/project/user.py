"""
8.	Library*

Create a class called Library, where the information regarding the users and books rented/available will be stored.
Create another one called User, where the information for each of the library users will be stored,
and Registration class, where user information will be administrated (created/edited/deleted)
and stored in the Library records.

Class User

In the user.py file, create class User.
Upon initialization, it should receive user_id (int) and username (string).

The class should also have an instance attribute books that is an empty list.

You should also create 2 instance methods:
-	info() - returns a string containing the books currently rented by the user in ascending order
separated by comma and space.

-	__str__() - override the method to get a string in the following format "{user_id}, {username},
 {list of rented books}"
"""


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'