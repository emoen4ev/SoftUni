# Generated by Django 4.1.2 on 2022-10-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0006_employee_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
