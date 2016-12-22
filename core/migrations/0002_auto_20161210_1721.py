# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-10 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=512)),
                ('senha', models.CharField(max_length=128)),
                ('telefone', models.CharField(max_length=128)),
                ('endereco', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='core.Categoria'),
        ),
    ]