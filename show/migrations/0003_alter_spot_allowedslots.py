# Generated by Django 4.2.7 on 2023-11-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("show", "0002_spot_allowedslots_spot_created_by_spot_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spot",
            name="allowedSlots",
            field=models.CharField(default="", max_length=300),
        ),
    ]
