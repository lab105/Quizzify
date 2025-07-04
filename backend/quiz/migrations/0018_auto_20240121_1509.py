# Generated by Django 3.2.18 on 2024-01-21 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0017_noassistanceanswers_uid_no_promptedanswers_uid_no_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="uid",
            new_name="roll_no",
        ),
        migrations.RemoveField(
            model_name="noassistanceanswers",
            name="uid_no",
        ),
        migrations.RemoveField(
            model_name="noassistanceanswers",
            name="user_id",
        ),
        migrations.RemoveField(
            model_name="promptedanswers",
            name="uid_no",
        ),
        migrations.RemoveField(
            model_name="promptedanswers",
            name="user_id",
        ),
        migrations.RemoveField(
            model_name="unpromptedanswers",
            name="uid_no",
        ),
        migrations.RemoveField(
            model_name="unpromptedanswers",
            name="user_id",
        ),
        migrations.AddField(
            model_name="noassistanceanswers",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quiz.user"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="promptedanswers",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quiz.user"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="unpromptedanswers",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quiz.user"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
