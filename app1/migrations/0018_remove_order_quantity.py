# Generated by Django 4.1.5 on 2023-06-16 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_order_price_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
