# Generated by Django 4.1.5 on 2023-05-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_categories_id_categories_cat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='cat_id',
            field=models.IntegerField(default=10, unique=True),
        ),
    ]
