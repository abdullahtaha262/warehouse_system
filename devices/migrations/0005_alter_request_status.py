# Generated by Django 5.0.3 on 2024-09-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_alter_request_options_request_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied'), ('returned', 'Returned')], default='pending', max_length=20, verbose_name='Status'),
        ),
    ]
