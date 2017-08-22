# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170609_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name': 'Opcional',
                'verbose_name_plural': 'Opcionais',
            },
        ),
        migrations.CreateModel(
            name='Opcional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Opcionais', to='core.Empresa')),
            ],
            options={
                'verbose_name': 'Opcional',
                'verbose_name_plural': 'Opcionais',
            },
        ),
        migrations.AddField(
            model_name='opcao',
            name='opcional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Opcoes', to='core.Opcional'),
        ),
    ]
