# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-05 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20170504_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='BairroAtendimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('frete', models.FloatField(default=0)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bairro')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BairrosAtendimento', to='core.Empresa')),
            ],
            options={
                'verbose_name': 'Bairro de Atendimento',
                'verbose_name_plural': 'Bairros de Atendimento',
            },
        ),
    ]
