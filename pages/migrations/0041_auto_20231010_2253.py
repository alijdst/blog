# Generated by Django 3.2.21 on 2023-10-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0040_alter_posts_image'),
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
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='default.jpg', help_text='Post Picture', upload_to='media'),
        ),
    ]