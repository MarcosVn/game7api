# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-09 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170608_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Bairro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cidade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='face_id',
            field=models.CharField(default=None, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]