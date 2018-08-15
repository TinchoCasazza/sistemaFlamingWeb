# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Detalle', models.CharField(max_length=50)),
                ('PrecioVenta', models.DecimalField(max_digits=7, decimal_places=2)),
                ('PrecioCosto', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='Id',
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
