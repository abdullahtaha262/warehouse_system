# Generated by Django 5.0.3 on 2024-09-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_product_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True, verbose_name='Serial Number'),
        ),
    ]
