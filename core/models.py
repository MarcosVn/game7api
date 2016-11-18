#  -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Estado:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __unicode__(self):
        return str(self.nome)


class Cidade:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    estado = models.ForeignKey("Estado", related_name="cidades")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __unicode__(self):
        return str(self.nome)


class Bairro:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    cidade = models.ForeignKey("Cidade", related_name="bairros")

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __unicode__(self):
        return str(self.nome)


class Empresa:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=1024)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=128)
    bairros = models.ManyToManyField("Bairro", related_name="empresas")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return str(self.nome)


class Cobranca:
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=512)
    data_inicio = models.DateField(auto_now=True)
    data_fim = models.DateField(null=True)
    total = models.FloatField()
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cobrança"
        verbose_name_plural = "Cobranças"

    def __unicode__(self):
        return str(self.referencia)


class Cliente:
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    endereco = models.CharField(max_length=512)
    cidade = models.ForeignKey("Cidade")
    bairro = models.ForeignKey("Bairro")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return str(self.nome)


# class Cardapio:
#     id = models