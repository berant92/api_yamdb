# Generated by Django 3.2 on 2023-01-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230121_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='me',
            field=models.TextField(null=True),
        ),
    ]
