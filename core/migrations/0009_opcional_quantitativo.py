# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170615_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcional',
            name='quantitativo',
            field=models.BooleanField(default=False),
        ),
    ]
