# Generated by Django 4.2.1 on 2023-05-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="dob",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="gender",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
