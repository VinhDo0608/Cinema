# Generated by Django 5.0.1 on 2024-02-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_reservation_movie_alter_reservation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='total_price',
        ),
        migrations.AddField(
            model_name='reservation',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default='cash', max_length=20),
        ),
    ]