# Generated by Django 3.2.21 on 2023-10-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0042_auto_20231010_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
    ]
