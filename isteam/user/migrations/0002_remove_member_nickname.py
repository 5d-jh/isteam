# Generated by Django 3.0.8 on 2020-08-21 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='nickname',
        ),
    ]
