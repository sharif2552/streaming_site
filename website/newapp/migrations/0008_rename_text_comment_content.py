# Generated by Django 4.1.3 on 2023-07-21 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_remove_comment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
    ]