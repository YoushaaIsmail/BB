# Generated by Django 5.0.2 on 2024-02-23 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about_us_images/')),
            ],
        ),
        migrations.CreateModel(
            name='categoriesPRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecategorie', models.CharField(max_length=100)),
                ('imagecategorie', models.ImageField(upload_to='categories_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(upload_to='product_images/')),
                ('image3', models.ImageField(upload_to='product_images/')),
                ('image4', models.ImageField(upload_to='product_images/')),
                ('image5', models.ImageField(upload_to='product_images/')),
                ('details', models.TextField()),
                ('categories1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blue.categoriesproduct')),
            ],
        ),
    ]
