# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 18:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumo', '0018_auto_20170722_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='data',
            field=models.DateField(default=datetime.date(2017, 7, 24)),
        ),
    ]
