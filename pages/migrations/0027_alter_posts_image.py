# Generated by Django 3.2.21 on 2023-10-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
