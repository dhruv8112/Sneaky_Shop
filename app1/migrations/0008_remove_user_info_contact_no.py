# Generated by Django 4.1.5 on 2023-06-04 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='contact_no',
        ),
    ]