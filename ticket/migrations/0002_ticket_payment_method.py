# Generated by Django 5.0.1 on 2024-02-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default='cash', max_length=20),
        ),
    ]