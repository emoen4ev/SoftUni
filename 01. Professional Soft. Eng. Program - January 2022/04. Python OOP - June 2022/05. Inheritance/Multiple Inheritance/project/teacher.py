"""
3.	Multiple Inheritance_old

In a folder called project_old create three files: person.py, employee.py, and teacher.py.

In each file, create its corresponding class - Person, Employee, and Teacher:
•	Person with a single method sleep() that returns: "sleeping..."
•	Employee with a single method get_fired() that returns: "fired..."
•	Teacher with a single method teach() that returns: "teaching...".

Teacher should inherit from Person and Employee.

Submit in Judge a zip file of the folder project_old.
"""


from person import Person
from employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'