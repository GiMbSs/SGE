# Generated by Django 5.2.1 on 2025-05-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                blank=True, null=True, upload_to='media/images/'
            ),
        ),
    ]
