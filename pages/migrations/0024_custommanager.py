# Generated by Django 3.2.20 on 2023-09-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_posts_is_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
