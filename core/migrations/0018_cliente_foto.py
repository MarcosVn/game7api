# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20171019_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
    ]