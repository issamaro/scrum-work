# Generated by Django 4.2.6 on 2023-10-19 19:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ichec", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Courses",
            new_name="Course",
        ),
        migrations.RenameModel(
            old_name="Masters",
            new_name="Master",
        ),
    ]
