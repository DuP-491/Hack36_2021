# Generated by Django 3.1.7 on 2021-04-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='cdefault.jpg', upload_to='courses'),
        ),
    ]
