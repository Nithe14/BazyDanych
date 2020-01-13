# Generated by Django 3.0.2 on 2020-01-13 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200113_1957'),
        ('opinions', '0011_auto_20200113_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
