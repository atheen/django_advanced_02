# Generated by Django 2.1.5 on 2020-09-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='slug',
        ),
    ]
