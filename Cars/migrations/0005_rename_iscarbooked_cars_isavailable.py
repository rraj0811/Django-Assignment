# Generated by Django 4.1.1 on 2022-11-07 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cars", "0004_rename_costperhour_cars_costperday"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cars",
            old_name="IsCarBooked",
            new_name="IsAvailable",
        ),
    ]
