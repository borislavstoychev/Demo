# Generated by Django 3.2.9 on 2021-11-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='demo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
