# Generated by Django 4.2.7 on 2023-11-28 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("show", "0005_timeslot_alter_show_artist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="show",
            name="time",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="show.timeslot"
            ),
        ),
    ]
