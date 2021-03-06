# Generated by Django 3.0.2 on 2020-01-05 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_producer_id'),
        ('orders', '0007_auto_20200105_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersproducts',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
