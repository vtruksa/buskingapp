# Generated by Django 4.2.7 on 2023-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("show", "0006_alter_show_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="show",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
