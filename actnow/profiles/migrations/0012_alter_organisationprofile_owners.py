# Generated by Django 3.2.5 on 2021-08-09 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profiles", "0011_profile_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisationprofile",
            name="owners",
            field=models.ManyToManyField(
                related_name="organisations", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
