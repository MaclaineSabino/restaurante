# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumo', '0006_auto_20170703_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemconta',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
