# Generated by Django 4.1.3 on 2023-07-21 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]