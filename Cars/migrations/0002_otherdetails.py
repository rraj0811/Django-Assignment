# Generated by Django 4.1.1 on 2022-11-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="otherDetails",
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
                ("username", models.CharField(max_length=100)),
                ("Address", models.TextField()),
                ("phonenumber", models.CharField(max_length=10)),
            ],
        ),
    ]
