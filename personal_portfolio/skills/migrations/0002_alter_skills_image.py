# Generated by Django 4.1.2 on 2023-05-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='image',
            field=models.ImageField(upload_to='skills/images/'),
        ),
    ]
