# Generated by Django 3.0.2 on 2020-01-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200105_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('producer', models.CharField(default='', max_length=150)),
                ('ex_date', models.DateTimeField()),
                ('barcode', models.BigIntegerField(unique=True)),
                ('dose', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='ex_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='producer_id',
        ),
        migrations.AddField(
            model_name='product',
            name='pharm_form',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.DeleteModel(
            name='producer',
        ),
    ]