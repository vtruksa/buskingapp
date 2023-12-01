# Generated by Django 4.2.7 on 2023-11-28 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("show", "0003_alter_spot_allowedslots"),
    ]

    operations = [
        migrations.CreateModel(
            name="Show",
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
                ("time", models.DateTimeField()),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "spot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="show.spot"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="spot",
            name="shows_future",
            field=models.ManyToManyField(related_name="show_f", to="show.show"),
        ),
        migrations.AddField(
            model_name="spot",
            name="shows_past",
            field=models.ManyToManyField(related_name="show_p", to="show.show"),
        ),
    ]