# Generated by Django 3.1.3 on 2020-12-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_auto_20201201_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
