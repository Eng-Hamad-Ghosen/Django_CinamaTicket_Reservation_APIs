# Generated by Django 5.0.7 on 2024-08-04 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_rename_guste_guest_rename_guste_reservation_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_guest', to='ticket.guest'),
        ),
    ]
