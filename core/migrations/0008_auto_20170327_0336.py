# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 03:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_pedido_componente_entrega'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='componente_entrega',
            new_name='complemento_entrega',
        ),
    ]
