# Generated by Django 5.0.1 on 2024-01-29 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
