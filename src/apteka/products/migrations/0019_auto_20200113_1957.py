# Generated by Django 3.0.2 on 2020-01-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200113_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleproduct',
            name='id',
        ),
        migrations.AlterField(
            model_name='simpleproduct',
            name='barcode',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
