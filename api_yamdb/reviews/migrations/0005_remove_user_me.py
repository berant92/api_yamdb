# Generated by Django 3.2 on 2023-01-22 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_user_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='me',
        ),
    ]
