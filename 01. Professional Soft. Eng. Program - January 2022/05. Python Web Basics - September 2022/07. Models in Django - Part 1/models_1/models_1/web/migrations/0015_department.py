# Generated by Django 4.1.2 on 2022-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0014_alter_employee_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=15)),
            ],
        ),
    ]
