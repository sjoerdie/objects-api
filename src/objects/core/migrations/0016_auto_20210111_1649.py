# Generated by Django 2.2.12 on 2021-01-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_objectrecord_geometry"),
    ]

    operations = [
        migrations.RenameField(
            model_name="objectrecord", old_name="end_date", new_name="end_at"
        ),
        migrations.RenameField(
            model_name="objectrecord",
            old_name="registration_date",
            new_name="registration_at",
        ),
        migrations.RenameField(
            model_name="objectrecord",
            old_name="start_date",
            new_name="start_at",
        ),
    ]