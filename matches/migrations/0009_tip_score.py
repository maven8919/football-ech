# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0008_auto_20160524_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
