# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-05 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_bairroatendimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='bairros_atendimento',
        ),
    ]
