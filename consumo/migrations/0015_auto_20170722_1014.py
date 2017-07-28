# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumo', '0014_auto_20170721_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='data',
            field=models.DateField(default=datetime.date(2017, 7, 22)),
        ),
        migrations.AlterField(
            model_name='conta',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]