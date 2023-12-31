# Generated by Django 4.2.4 on 2023-08-10 05:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=16, region=None)),
                ('email', models.EmailField(max_length=64)),
            ],
        ),
    ]
