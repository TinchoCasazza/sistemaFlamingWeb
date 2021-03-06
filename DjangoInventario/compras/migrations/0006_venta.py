# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_tipopago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('Compras', models.IntegerField()),
                ('ExistenciaFinal', models.IntegerField()),
                ('CostoUnidades', models.IntegerField()),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Costo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compras.Producto')),
            ],
        ),
    ]
