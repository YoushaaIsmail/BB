# Generated by Django 5.0.2 on 2024-02-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blue', '0003_alter_product_image3_alter_product_image4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
