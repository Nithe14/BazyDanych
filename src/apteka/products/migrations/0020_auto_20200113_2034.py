# Generated by Django 3.0.2 on 2020-01-13 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200113_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simpleproduct',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='simpleproduct',
            name='dose',
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]