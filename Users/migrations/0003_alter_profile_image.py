# Generated by Django 4.1.3 on 2022-11-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.jpg', upload_to='user_pics'),
        ),
    ]