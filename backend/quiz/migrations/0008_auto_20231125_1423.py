# Generated by Django 3.2.18 on 2023-11-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_auto_20231122_1811"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useranswers",
            name="continue_button_click_time",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="help_button_click_time",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="is_correct",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="option_chosen",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="option_click_time",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="question_number",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="set_attempted",
        ),
        migrations.RemoveField(
            model_name="useranswers",
            name="time_spent_on_question",
        ),
        migrations.AddField(
            model_name="useranswers",
            name="action",
            field=models.CharField(
                choices=[
                    ("A", "A"),
                    ("B", "B"),
                    ("C", "C"),
                    ("D", "D"),
                    ("Start", "Start"),
                    ("End", "End"),
                    ("Prompt", "Prompt"),
                    ("Continue", "Continue"),
                ],
                default="Null",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="useranswers",
            name="page",
            field=models.CharField(default="Null", max_length=200),
        ),
        migrations.AddField(
            model_name="useranswers",
            name="time",
            field=models.TimeField(default="00:00"),
        ),
        migrations.AlterField(
            model_name="useranswers",
            name="user_id",
            field=models.IntegerField(),
        ),
    ]
