# Generated by Django 3.0.2 on 2020-01-04 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('recived', models.CharField(default='', max_length=150)),
                ('payment', models.CharField(default='', max_length=150)),
                ('status', models.CharField(default='', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
