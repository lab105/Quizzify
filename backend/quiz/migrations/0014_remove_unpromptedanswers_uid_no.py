# Generated by Django 4.2.6 on 2023-12-04 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0013_unpromptedanswers_uid_no_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="unpromptedanswers",
            name="uid_no",
        ),
    ]
