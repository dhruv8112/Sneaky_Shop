# Generated by Django 4.1.5 on 2023-06-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('Email', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=25)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=110, null=True)),
                ('pro_id', models.IntegerField(null=True, unique=True)),
                ('pro_name', models.CharField(max_length=200)),
                ('Pro_Description', models.CharField(default='Default description', max_length=2000)),
                ('size', models.IntegerField(null=True)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='ProductImage')),
            ],
        ),
        migrations.DeleteModel(
            name='categories',
        ),
    ]