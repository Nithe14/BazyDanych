# Generated by Django 3.0.2 on 2020-01-08 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200108_1635'),
        ('orders', '0006_auto_20200108_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersproducts',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
