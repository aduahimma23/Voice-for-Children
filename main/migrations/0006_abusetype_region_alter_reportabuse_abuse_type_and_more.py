# Generated by Django 5.0.1 on 2024-03-23 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_remove_reportabuse_add_new_abuse_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbuseType",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="reportabuse",
            name="abuse_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.abusetype"
            ),
        ),
        migrations.AlterField(
            model_name="reportabuse",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.region"
            ),
        ),
    ]
