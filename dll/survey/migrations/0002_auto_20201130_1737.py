# Generated by Django 2.2.17 on 2020-11-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyquestion",
            name="position",
            field=models.PositiveIntegerField(default=0, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="surveyquestionchoice",
            name="position",
            field=models.PositiveIntegerField(default=0, verbose_name="Position"),
        ),
    ]
