# Generated by Django 4.1.3 on 2023-07-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
