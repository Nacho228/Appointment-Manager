# Generated by Django 5.0.1 on 2024-01-31 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogMessage',
        ),
    ]
