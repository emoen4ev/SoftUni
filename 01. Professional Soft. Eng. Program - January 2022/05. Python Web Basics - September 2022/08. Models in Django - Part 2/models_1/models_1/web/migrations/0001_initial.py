# Generated by Django 4.1.2 on 2022-10-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("years_of_experience", models.IntegerField()),
                ("years_of_experience_positive", models.PositiveIntegerField()),
                ("review", models.TextField()),
                ("start_date", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
