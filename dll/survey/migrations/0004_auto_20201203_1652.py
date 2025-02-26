# Generated by Django 2.2.17 on 2020-12-03 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0003_trigger_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="surveyquestionchoice",
            options={"ordering": ["position"]},
        ),
        migrations.AlterField(
            model_name="surveyquestion",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="survey_questions",
                to="survey.Survey",
            ),
        ),
        migrations.AlterField(
            model_name="surveyquestionchoice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="choices",
                to="survey.SurveyQuestion",
            ),
        ),
        migrations.AlterField(
            model_name="trigger",
            name="event",
            field=models.CharField(
                choices=[
                    ("pageOpen", "Open Page"),
                    ("leaveIntent", "Leave Intent"),
                    ("content-submission", "Content Submission"),
                ],
                max_length=64,
                verbose_name="Trigger Type",
            ),
        ),
        migrations.AlterField(
            model_name="trigger",
            name="url",
            field=models.CharField(
                blank=True, max_length=512, null=True, verbose_name="Page Url"
            ),
        ),
    ]
