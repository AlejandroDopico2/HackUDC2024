# Generated by Django 5.0.2 on 2024-02-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="", max_length=20),
        ),
    ]
