# Generated by Django 3.0 on 2021-05-20 01:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0009_auto_20210520_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_course',
            name='year_of_study',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
    ]
