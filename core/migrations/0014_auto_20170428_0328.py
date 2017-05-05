# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-28 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170409_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandeira',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('tipo', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Bandeira',
                'verbose_name_plural': 'Bandeiras',
            },
        ),
        migrations.AddField(
            model_name='pagamento',
            name='trocopara',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]