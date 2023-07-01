# Generated by Django 4.2.2 on 2023-07-01 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(max_length=500)),
                ("day", models.DateField(db_index=True)),
                ("hours", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("trainers", models.CharField(max_length=200)),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.club"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "classes",
            },
        ),
    ]