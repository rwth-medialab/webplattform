# Generated by Django 2.2.4 on 2019-09-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_auto_20190905_1109"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dlluser",
            name="additional_emails",
        ),
    ]
