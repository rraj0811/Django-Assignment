# Generated by Django 4.1.1 on 2022-11-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cars", "0002_otherdetails"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="CostPerHour",
            field=models.IntegerField(default=5000),
        ),
    ]
