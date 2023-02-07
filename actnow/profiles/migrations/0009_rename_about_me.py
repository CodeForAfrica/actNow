# Generated by Django 3.2.5 on 2021-08-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0008_reorganise_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisationprofile",
            name="bio",
            field=models.TextField(blank=True, max_length=255, verbose_name="bio"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(blank=True, max_length=255, verbose_name="bio"),
        ),
    ]
