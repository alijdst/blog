# Generated by Django 3.2.21 on 2023-10-10 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20231010_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image_width',
        ),
    ]
