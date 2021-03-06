# Generated by Django 3.0.2 on 2020-01-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField(verbose_name=45)),
                ('category', models.TextField(verbose_name=45)),
                ('ingredients', models.TextField(verbose_name=45)),
                ('ex_date', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
