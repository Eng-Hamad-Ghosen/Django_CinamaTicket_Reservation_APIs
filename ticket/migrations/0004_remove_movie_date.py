# Generated by Django 5.0.6 on 2024-08-08 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_reservation_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]
