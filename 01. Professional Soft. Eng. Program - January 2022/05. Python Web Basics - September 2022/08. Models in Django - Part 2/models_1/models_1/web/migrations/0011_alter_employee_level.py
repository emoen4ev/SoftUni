# Generated by Django 4.1.2 on 2022-10-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0010_employee_is_full_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="level",
            field=models.CharField(
                choices=[("jr", "Junior"), ("reg", "Regular"), ("sr", "Senior")],
                max_length=3,
            ),
        ),
    ]
