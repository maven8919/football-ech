# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20160504_1134'),
        ('matches', '0002_tip'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
    ]
