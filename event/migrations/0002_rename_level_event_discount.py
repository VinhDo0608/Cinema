# Generated by Django 5.0.1 on 2024-02-02 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='level',
            new_name='discount',
        ),
    ]