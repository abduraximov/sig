# Generated by Django 4.2.4 on 2023-08-11 12:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leak",
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
                ("name", models.CharField(max_length=64)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=16, region=None
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leak",
                        to="base.account",
                    ),
                ),
            ],
        ),
    ]