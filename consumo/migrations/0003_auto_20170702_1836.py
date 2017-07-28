# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumo', '0002_auto_20170629_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conta',
            name='data',
            field=models.DateField(default=datetime.date(2017, 7, 2)),
        ),
    ]