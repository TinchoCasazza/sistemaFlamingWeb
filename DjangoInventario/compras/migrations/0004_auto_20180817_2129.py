# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_producto_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Detalle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]