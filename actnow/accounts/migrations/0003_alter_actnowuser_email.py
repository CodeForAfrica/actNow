# Generated by Django 3.2.3 on 2021-06-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_actnow_user_match_abstract_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actnowuser",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
