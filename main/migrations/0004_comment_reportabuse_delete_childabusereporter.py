# Generated by Django 5.0.1 on 2024-03-23 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_donation_payment_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("full_text", models.TextField()),
                ("sent_at", models.DateTimeField(auto_now_add=True)),
                (
                    "contct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.contact"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportAbuse",
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
                ("add_new_region", models.CharField(default="add new", max_length=50)),
                (
                    "add_new_abuse_type",
                    models.CharField(default="add new", max_length=100),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                ("child_name", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                (
                    "abuse_type",
                    models.CharField(
                        choices=[
                            ("physical", "Physical Abuse"),
                            ("emotional", "Emotional Abuse"),
                            ("sexual", "Sexual Abuse"),
                            ("neglect", "Neglect"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("ashanti", "Ashanti Region"),
                            ("brong-ahafo", "Brong-Ahafo Region"),
                            ("central", "Central Region"),
                        ],
                        max_length=50,
                    ),
                ),
                ("town", models.CharField(max_length=100)),
                ("support_needed", models.TextField()),
                ("sub_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="ChildAbuseReporter",
        ),
    ]
