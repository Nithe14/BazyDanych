# Generated by Django 3.0.2 on 2020-01-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200105_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(),
        ),
    ]
