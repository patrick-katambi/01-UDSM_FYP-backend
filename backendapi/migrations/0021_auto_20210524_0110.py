# Generated by Django 3.0 on 2021-05-24 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapi', '0020_auto_20210524_0056'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lecture_course',
            unique_together={('lecturer', 'course', 'academic_year')},
        ),
    ]
