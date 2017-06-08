#  -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    cep = models.CharField(max_length=15, default="")
    endereco = models.CharField(max_length=512)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=512, default="")
    bairro = models.ForeignKey("Bairro")
    telefone = models.CharField(max_length=128)
    descricao = models.CharField(max_length=1024)
    tipocozinha = models.ForeignKey("TipoCozinha", null=True)
    nota = models.FloatField(default=0)
    ttl_avaliacoes = models.IntegerField(default=0)
    custo = models.ForeignKey("TipoPreco", null=True)
    tempo = models.ForeignKey("TipoTempo", null=True)
    nota_atual = models.FloatField(default=0.0)
    aceita_cartao = models.BooleanField(default=False)
    aceita_valerefeicao = models.BooleanField(default=False)
    aceita_pagamentoonline = models.BooleanField(default=False)
    status = models.CharField(max_length=512, default="ok")
    porcentagem_repasse = models.FloatField(default=12)
    logotipo = models.CharField(max_length=1024, default="sem-logo.jpg")
    valor_mensalidade = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return str(self.nome)

class BairroAtendimento(models.Model):
    id = models.AutoField(primary_key=True)
    bairro = models.ForeignKey(Bairro)
    empresa = models.ForeignKey(Empresa, related_name="BairrosAtendimento")
    frete = models.FloatField(default=0.0)
    class Meta:
        verbose_name = "Bairro de Atendimento"
        verbose_name_plural = "Bairros de Atendimento"

    def __unicode__(self):
        return str(self.bairro.nome)

class Repasse(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=512)
    data_inicio = models.DateField(auto_now=True)
    data_fim = models.DateField(null=True)
    data_pagamento = models.DateField(null=True)
    data_bloqueio = models.DateField(null=True)
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
    senha = models.CharField(max_length=128, null=True)
    telefone = models.CharField(max_length=128, null=True)
    cep = models.CharField(max_length=15, default="", null=True)
    endereco = models.CharField(max_length=512, null=True)
    cidade = models.ForeignKey("Cidade", null=True)
    bairro = models.ForeignKey("Bairro", null=True)
    numero = models.IntegerField(default=0, null=True)
    complemento = models.CharField(max_length=512, default="", null=True)
    face_id = models.CharField(max_length=1024, null=True)

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

class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade=models.IntegerField(default=1)
    produto = models.ForeignKey("Produto")
    observacao = models.CharField(max_length=1024, null=True)
    cliente = models.ForeignKey("Cliente")

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def __unicode__(self):
        return str(self.produto.nome)

class Bandeira(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    tipo = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Bandeira"
        verbose_name_plural = "Bandeiras"
    def __unicode__(self):
        return self.titulo

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(auto_now=True)
    total = models.FloatField()
    cliente = models.ForeignKey("Cliente", related_name="Pedidos")
    empresa = models.ForeignKey("Empresa", related_name="Pedidos")
    status = models.CharField(default="Aguardando Endereco", null=True, max_length=512)
    endereco_entrega = models.CharField(max_length=512)
    cidade_entrega = models.ForeignKey("Cidade")
    bairro_entrega = models.ForeignKey("Bairro")
    complemento_entrega = models.CharField(max_length=512)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __unicode__(self):
        return self.cliente.nome + "_" + str(self.id)

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.FloatField()
    pedido = models.ForeignKey("Pedido", related_name="Pagamento")
    tipopagamento = models.CharField(max_length=512)
    obs = models.CharField(max_length=512)
    trocopara = models.FloatField(default=0.0)
    cpfnanota = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __unicode__(self):
        return self.obs

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey("Pedido", null=True, related_name="Avaliacoes")
    nota = models.IntegerField(default=0)
    data = models.DateField(auto_now=True)
    mensagem = models.CharField(max_length=1024, null=True, blank=True)

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
    observacao = models.CharField(max_length=1024, null=True)

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

class Mensalidade(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField(default=0.0)
    titulo = models.CharField(max_length=512)
    empresa = models.ForeignKey("Empresa", related_name="Mensalidades")
    data_pagamento = models.DateField(null=True)
    data_cobranca = models.DateField(auto_now=True)
    status = models.CharField(max_length=512, default="Aguardando Pagamento")
    class Meta:
        verbose_name = "Mensalidade"
        verbose_name_plural = "Mensalidades"

    def __unicode__(self):
        return self.titulo
