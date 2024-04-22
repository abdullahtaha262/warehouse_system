# Generated by Django 5.0.3 on 2024-04-20 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='المنتجات',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم', models.CharField(max_length=255)),
                ('الفئة', models.CharField(choices=[('laptop', 'لابتوب'), ('desktop', 'ديسكتوب'), ('server', 'سيرفر'), ('accessory', 'ملحقات')], default='لابتوب', max_length=100)),
                ('الصناعة', models.CharField(max_length=255)),
                ('الموديل', models.CharField(max_length=255)),
                ('الرقم_المتسلسل', models.CharField(max_length=100, unique=True)),
                ('الوصف', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='المخزون',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الكمية', models.IntegerField()),
                ('المنتجات', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.المنتجات')),
            ],
        ),
    ]