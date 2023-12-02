# Generated by Django 4.2.7 on 2023-12-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("show", "0007_show_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                (
                    "show",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="show.show"
                    ),
                ),
            ],
        ),
    ]
