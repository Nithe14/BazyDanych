# Generated by Django 3.0.2 on 2020-01-04 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0011_auto_20200104_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
