# Generated by Django 5.1.2 on 2024-11-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
