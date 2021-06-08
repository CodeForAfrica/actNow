# Generated by Django 3.2.3 on 2021-06-08 09:20
from typing import List

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: List[str]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=255, null=True, verbose_name="About me"
                    ),
                ),
                ("location", models.TextField()),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'.        Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("socials", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
