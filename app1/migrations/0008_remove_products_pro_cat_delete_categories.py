# Generated by Django 4.1.5 on 2023-06-01 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_categories_cat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='pro_cat',
        ),
        migrations.DeleteModel(
            name='categories',
        ),
    ]