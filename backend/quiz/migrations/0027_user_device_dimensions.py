# Generated by Django 4.2.6 on 2024-02-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0026_feedbackans_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="device_dimensions",
            field=models.TextField(default="0x0"),
        ),
    ]
