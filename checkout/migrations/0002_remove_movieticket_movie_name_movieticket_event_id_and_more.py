# Generated by Django 5.0.1 on 2024-01-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieticket',
            name='movie_name',
        ),
        migrations.AddField(
            model_name='movieticket',
            name='event_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='movieticket',
            name='movie_id',
            field=models.IntegerField(default=1),
        ),
    ]
