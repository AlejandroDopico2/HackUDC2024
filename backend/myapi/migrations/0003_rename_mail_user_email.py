# Generated by Django 5.0.2 on 2024-02-17 00:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0002_user_password"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="mail",
            new_name="email",
        ),
    ]
