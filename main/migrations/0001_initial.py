# Generated by Django 4.2.7 on 2023-11-28 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                ("f_name", models.CharField(max_length=50)),
                ("l_name", models.CharField(max_length=50)),
                ("gear", models.TextField(null=True)),
                ("bio", models.TextField(null=True)),
                ("link_ig", models.CharField(max_length=128, null=True)),
                ("link_fb", models.CharField(max_length=128, null=True)),
                ("link_x", models.CharField(max_length=128, null=True)),
                ("link_tt", models.CharField(max_length=128, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
