#  -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Empresa:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=1024)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return str(self.nome)


class Usuario:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    empresa = models.ForeignKey("Empresa", related_name="funcionarios")
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return str(self.nome)
