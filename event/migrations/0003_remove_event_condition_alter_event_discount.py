# Generated by Django 5.0.1 on 2024-02-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_rename_level_event_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='condition',
        ),
        migrations.AlterField(
            model_name='event',
            name='discount',
            field=models.SmallIntegerField(),
        ),
    ]
