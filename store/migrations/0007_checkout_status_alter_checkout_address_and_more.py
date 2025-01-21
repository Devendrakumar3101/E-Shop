# Generated by Django 5.1.4 on 2025-01-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
