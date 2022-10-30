from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

'''
•	Profile
    o	Username
        	Character field, required.
        	It should consist of a maximum of 10 characters.
        	It should consist of a minimum of 2 characters.
            Otherwise, raise a ValidationError with the message: "The username must be a minimum of 2 chars" 
    o	Email
        	Email field, required.
    o	Age
        	Integer field, required.
        	The age cannot be below 18.
    o	Password
        	Character (password) field, required.
        	It should consist of a maximum of 30 characters.
    o	First Name
        	Character field, optional.
        	It should consist of a maximum of 30 characters.
    o	Last Name
        	Character field, optional.
        	It should consist of a maximum of 30 characters.
    o	Profile Picture
        	URL field, optional.
•	Car
    o	Type
        	Character (choice) field, required.
        	It should consist of a maximum of 10 characters.
        	The choices are "Sports Car", "Pickup", "Crossover", "Minibus" and "Other".
    o	Model
        	Character field, required.
        	It should consist of a maximum of 20 characters.
        	It should consist of a minimum of 2 characters.
    o	Year
        	Integer field, required.
        	Valid year is a year between 1980 and 2049 (both inclusive). 
            Otherwise, raise a ValidationError with the message: "Year must be between 1980 and 2049"
    o	Image Url
        	URL field, required.
    o	Price
        	Float field, required.
        	Price cannot be below 1.	
Note: the validations will be examined only by the user side, not the admin side.

'''
MIN_USERNAME_LENGTH = 2

MIN_YEAR = 1980
MAX_YEAR = 2049


def validate_username_min_length(value):
    if len(value) < MIN_USERNAME_LENGTH:
        raise exceptions.ValidationError('The username must be a minimum of 2 chars')


def validate_years_range(value):
    if value not in range(MIN_YEAR, MAX_YEAR + 1):
        raise exceptions.ValidationError('Year must be between 1980 and 2049')


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 10

    MIN_AGE = 18

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            validate_username_min_length,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    class Car(models.Model):
        MAX_MODEL_NAME_LENGTH = 20
        MIN_MODEL_NAME_LENGTH = 2

        MIN_PRICE_VALUE = 1

        SPORTS_CAR = 'Sports Car'
        PICKUP = 'Pickup'
        CROSSOVER = 'Crossover'
        MINIBUS = 'Minibus'
        OTHER = 'Other'

        CAR_TYPES = (
            (SPORTS_CAR, SPORTS_CAR),
            (PICKUP, PICKUP),
            (CROSSOVER, CROSSOVER),
            (MINIBUS, MINIBUS),
            (OTHER, OTHER),
        )

        # CAR_TYPES = ([(types, types) for types in (SPORTS_CAR, PICKUP, CROSSOVER, MINIBUS, OTHER)])

        type = models.CharField(
            max_length=10,
            choices=CAR_TYPES,
            null=False,
            blank=False,
        )

        model = models.CharField(
            max_length=MAX_MODEL_NAME_LENGTH,
            validators=(
                MinLengthValidator(MIN_MODEL_NAME_LENGTH),
            ),
            null=False,
            blank=False,
        )

        year = models.IntegerField(
            validators=(
                validate_years_range,
            ),
            null=False,
            blank=False,
        )

        image_url = models.URLField(
            null=False,
            blank=False,
        )

        price = models.FloatField(
            validators=(
                MinValueValidator(MIN_PRICE_VALUE),
            ),
            null=False,
            blank=False,
        )