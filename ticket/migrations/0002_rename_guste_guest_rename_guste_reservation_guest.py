# Generated by Django 5.0.7 on 2024-08-04 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guste',
            new_name='Guest',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='guste',
            new_name='guest',
        ),
    ]
