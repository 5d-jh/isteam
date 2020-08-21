# Generated by Django 3.0.8 on 2020-08-21 04:09

from django.db import migrations, models
import groupware.models


class Migration(migrations.Migration):

    dependencies = [
        ('groupware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'FIRST'), (2, 'SECOND')], default=groupware.models.Semester['FIRST'])),
                ('embedded_link', models.CharField(max_length=200)),
            ],
        ),
    ]
