# Generated by Django 4.0.5 on 2023-05-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_remove_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]