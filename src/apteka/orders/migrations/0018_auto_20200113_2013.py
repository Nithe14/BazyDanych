# Generated by Django 3.0.2 on 2020-01-13 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200113_1957'),
        ('orders', '0017_auto_20200113_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersproducts',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]