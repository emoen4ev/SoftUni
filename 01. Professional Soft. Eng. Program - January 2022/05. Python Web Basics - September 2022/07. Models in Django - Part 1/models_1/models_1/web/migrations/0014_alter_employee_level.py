# Generated by Django 4.1.2 on 2022-10-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0013_alter_employee_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="level",
            field=models.CharField(
                choices=[
                    ("Junior", "Junior"),
                    ("Regular", "Regular"),
                    ("Senior", "Senior"),
                ],
                max_length=7,
                verbose_name="Seniority level",
            ),
        ),
    ]
