# Generated by Django 3.1.7 on 2021-04-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
    ]
