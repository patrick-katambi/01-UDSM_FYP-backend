# Generated by Django 3.0 on 2021-06-28 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0052_auto_20210603_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment_results',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
