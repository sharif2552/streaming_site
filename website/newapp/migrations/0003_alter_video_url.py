# Generated by Django 4.1.3 on 2023-07-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
