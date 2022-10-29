from enum import Enum

from django.db import models


# models.py

# Model fields == class attributes in Model classes


# class EmployeeLevel(Enum): # It's the best way ...
#     JUNIOR = 'Junior',
#     REGULAR = 'Regular',
#     SENIOR = 'Senior'

# One-to-many relationship
# Must migrate this first
class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk} / Name: {self.name}'


# Many-to-many relationship(only one migration needs)
class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    # Var char(30) => strings with max length of 30 characters
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    # level = models.CharField(
    #     max_length=3,
    #     choices=(
    #         ('jr', 'Junior'),
    #         ('reg', 'Regular'),
    #         ('sr', 'Senior'),
    #     )
    # )

    level = models.CharField(
        verbose_name='Seniority level',  # Only for visualisation
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
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

    is_full_time = models.BooleanField(
        null=True,
    )

    # is_full_time_1 = models.BooleanField()

    # This will be automatically set on each 'save'/'update'
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )

    email = models.EmailField(
        # Adds 'UNIQUE' constraint
        unique=True,
        # editable=False,
    )

    # One-to-many relationship
    # Migrate second, after migrating class Department
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        # on_delete=models.SET_NULL, # SET_NULL works only if null=True
        # null=True,
    )

    # Many-to-many relationship(only one migration needs, after creating class Project)
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
        # trough='EmployeesProjects',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        # return f'Id: {self.pk} / Name: {self.first_name} {self.last_name}' # without @property
        return f'Id: {self.pk} / Name: {self.fullname}'  # used @property


# One-to-one relationship
class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Name: {self.name}'


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT
    )

    date_joined = models.DateField(
        auto_now_add=True,
        # Additional info
    )


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
        blank=True,  # Form validation
        null=True,
    )

    default = models.IntegerField(
        blank=False,
        null=False,
    )


# emp.level == Employee.LEVEL_REGULAR


# Employee.objects.all()  # Select
# Employee.objects.create()  # Insert
# Employee.objects.filter()  # Select + Where
# Employee.objects.update()  # Update


'''
Django ORM (Object-relational mapping)
'''