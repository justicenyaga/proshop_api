# Generated by Django 4.0.5 on 2023-05-11 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', 'update_image_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
