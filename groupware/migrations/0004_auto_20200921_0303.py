# Generated by Django 3.0.8 on 2020-09-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupware', '0003_session_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.TextField(null=True),
        ),
    ]