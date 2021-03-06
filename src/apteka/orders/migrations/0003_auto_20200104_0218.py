# Generated by Django 3.0.2 on 2020-01-04 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200104_0218'),
        ('orders', '0002_ordersproducts_product_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrdersProducts',
            new_name='Orders_Products',
        ),
        migrations.AlterField(
            model_name='orders_products',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
