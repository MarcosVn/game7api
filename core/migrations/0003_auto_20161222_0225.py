# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161210_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Pedidos', to='core.Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='core.Empresa'),
            preserve_default=False,
        ),
    ]