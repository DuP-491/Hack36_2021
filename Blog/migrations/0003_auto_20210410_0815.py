# Generated by Django 3.1.7 on 2021-04-10 02:45

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_remove_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='demovid',
            field=embed_video.fields.EmbedVideoField(default='demo.mp4'),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank='True', max_length=100, null='True'),
            preserve_default='True',
        ),
    ]