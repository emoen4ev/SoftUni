# Generated by Django 4.1.2 on 2022-10-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_alter_employee_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="level",
            field=models.CharField(default="asd", max_length=15),
            preserve_default=False,
        ),
    ]
