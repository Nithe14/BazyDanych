# Generated by Django 3.0.2 on 2020-01-04 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200104_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producer_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Producer'),
        ),
    ]
