# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-13 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_opcional_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='preco',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
