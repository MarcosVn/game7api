# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-04 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170504_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Avaliacoes', to='core.Pedido'),
        ),
    ]