# Generated by Django 3.0 on 2021-05-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_lecturer_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='lecturer',
            new_name='id',
        ),
    ]
