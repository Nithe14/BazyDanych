# Generated by Django 3.0.2 on 2020-01-13 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200113_1208'),
        ('orders', '0011_auto_20200105_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersproducts',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]