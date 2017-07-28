# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumo', '0016_auto_20170722_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumo.Produto'),
        ),
        migrations.AlterField(
            model_name='tipoproduto',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
