# Generated by Django 4.1.1 on 2022-11-07 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cars", "0003_cars_costperhour"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cars",
            old_name="CostPerHour",
            new_name="CostPerDay",
        ),
    ]
