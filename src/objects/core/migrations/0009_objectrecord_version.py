# Generated by Django 2.2.12 on 2020-09-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_objectrecord_correct"),
    ]

    operations = [
        migrations.AddField(
            model_name="objectrecord",
            name="version",
            field=models.PositiveSmallIntegerField(
                default=0,
                help_text="Version of the OBJECTTYPE for data in the object record",
                verbose_name="version",
            ),
            preserve_default=False,
        ),
    ]