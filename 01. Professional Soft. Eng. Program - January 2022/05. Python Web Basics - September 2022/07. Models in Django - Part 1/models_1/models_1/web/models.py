from django.db import models


# models.py

# Model fields == class attributes in Model classes

class Employee(models.Model):
    # Var char(30) => strings with max length of 30 characters
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=15,
    )

    age = models.IntegerField(
        default=-1
    )

    # int
    years_of_experience = models.IntegerField()

    # int > 0
    years_of_experience_positive = models.PositiveIntegerField()

    # Text => strings with unlimited length
    review = models.TextField()

    start_date = models.DateField()  # This field is filled in manually,
    # not automatically, unlike next two examples below

    # This will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be automatically set on each 'save'/'update'
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )

    email = models.EmailField(
        # Adds 'UNIQUE' constraint
        unique=True,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        # return f'Id: {self.pk} / Name: {self.first_name} {self.last_name}' # without @property
        return f'Id: {self.pk} / Name: {self.fullname}'  # used @property


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )

    null = models.IntegerField(
        blank=False,
        null=True,
    )

    blank_null = models.IntegerField(
        blank=True, # Form validation
        null=True,
    )

    default = models.IntegerField(
        blank=False,
        null=False,
    )



'''
Django ORM (Object-relational mapping)
'''

# Employee.objects.all()  # Select
# Employee.objects.create()  # Insert
# Employee.objects.filter()  # Select + Where
# Employee.objects.update()  # Update