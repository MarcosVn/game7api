#  -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __unicode__(self):
        return str(self.nome)


class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    estado = models.ForeignKey("Estado", related_name="cidades")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __unicode__(self):
        return str(self.nome)


class Abertura(models.Model):
    id = models.AutoField(primary_key=True)
    abertura = models.DateTimeField()
    fechamento = models.DateTimeField(null=True)
    empresa = models.ForeignKey("Empresa", related_name="aberturas")

    class Meta:
        verbose_name = "Abertura"
        verbose_name_plural = "Aberturas"


class Bairro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    cidade = models.ForeignKey("Cidade", related_name="bairros")

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __unicode__(self):
        return str(self.nome)


class TipoCozinha(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Tipo de Cozinha"
        verbose_name_plural = "Tipos de Cozinha"

    def __unicode__(self):
        return str(self.nome)


class TipoPreco(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Tipo Preço"
        verbose_name_plural = "Tipos de Preço"

    def __unicode__(self):
        return str(self.nome)

class TipoTempo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Tipo de Tempo Médio"
        verbose_name_plural = "Tipos de Tempo Médio"

    def __unicode__(self):
        return str(self.nome)


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=128)
    cidade = models.ForeignKey("Cidade")
    endereco = models.CharField(max_length=512)
    bairro = models.ForeignKey("Bairro")
    bairros_atendimento = models.ManyToManyField("Bairro", related_name="empresas")
    telefone = models.CharField(max_length=128)
    descricao = models.CharField(max_length=1024)
    tipocozinha = models.ForeignKey("TipoCozinha", null=True)
    nota = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    custo = models.ForeignKey("TipoPreco", null=True)
    tempo = models.ForeignKey("TipoTempo", null=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return str(self.nome)


class Repasse(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=512)
    data_inicio = models.DateField(auto_now=True)
    data_fim = models.DateField(null=True)
    total = models.FloatField()
    pago = models.BooleanField(default=False)
    empresa = models.ForeignKey("Empresa", related_name="Repasses")

    class Meta:
        verbose_name = "Cobrança"
        verbose_name_plural = "Cobranças"

    def __unicode__(self):
        return str(self.referencia)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    endereco = models.CharField(max_length=512)
    cidade = models.ForeignKey("Cidade")
    bairro = models.ForeignKey("Bairro")
    # geometria = models.PointField(blank=True, null=True, srid=4326)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return str(self.nome)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return str(self.nome)


class SubCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey("Categoria", related_name="subcategorias")

    class Meta:
        verbose_name = "Subcategoria"
        verbose_name_plural = "SubCategorias"

    def __unicode__(self):
        return str(self.nome)


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    foto = models.CharField(max_length=1024)
    descricao = models.CharField(max_length=1024)
    preco = models.FloatField(null=True)
    empresa = models.ForeignKey("Empresa", related_name="produtos")
    subcategorias = models.ManyToManyField("SubCategoria", related_name="subcategorias")
    class Meta:
        verbose_name="Produto"
        verbose_name_plural="Produtos"

    def __unicode__(self):
        return str(self.nome)


class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    caminho = models.CharField(max_length=1024)
    produto = models.ForeignKey("Produto", related_name="fotos")

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __unicode__(self):
        return self.produto.nome + "_" + str(self.id)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(auto_now=True)
    total = models.FloatField()
    cliente = models.ForeignKey("Cliente", related_name="Pedidos")
    empresa = models.ForeignKey("Empresa", related_name="Pedidos")
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __unicode__(self):
        return self.cliente.nome + "_" + str(self.id)


class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey("Pedido", null=True, related_name="Avaliado")
    nota = models.IntegerField(default=0)
    data = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __unicode__(self):
        return str(self.nota)


class Item(models.Model):
    id=models.AutoField(primary_key=True)
    pedido=models.ForeignKey("Pedido", related_name="Itens")
    quantidade=models.IntegerField(default=1)
    produto = models.ForeignKey("Produto")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __unicode__(self):
        return self.produto.nome + "_" + str(self.id)


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    endereco = models.CharField(max_length=512)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def __unicode__(self):
        return str(self.nome)