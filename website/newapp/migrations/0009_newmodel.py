# Generated by Django 4.1.3 on 2023-07-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_rename_text_comment_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='newmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]