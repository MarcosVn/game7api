# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_empresa_bairro'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
