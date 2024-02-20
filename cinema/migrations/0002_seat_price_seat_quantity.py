# Generated by Django 5.0.1 on 2024-02-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='seat',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]