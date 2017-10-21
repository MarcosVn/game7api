# -*- coding:utf8
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from core.models import *
from django.template.context import RequestContext
from django.core.serializers import serialize
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode
from django.conf import settings
from datetime import *
import json
import base64
import random
import re
import mercadopago
import demjson
import hashlib
from mailer import Mailer
from mailer import Message

class politicaprivacidadeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('politica-privacidade.html', {}, RequestContext(request))
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('home.html', {}, RequestContext(request))
class sobreView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('sobre.html', {}, RequestContext(request))
class buscarView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('busca.html', {}, RequestContext(request))
class cadastrarLogarView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cadastro-login.html', {}, RequestContext(request))


class restauranteLoginView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-login.html', {}, RequestContext(request))
class restauranteHomeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-home.html', {}, RequestContext(request))
class restaurantePerfilView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-profile.html', {}, RequestContext(request))
class restauranteExpedienteView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-expediente.html', {}, RequestContext(request))
class restauranteCardapioView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio.html', {}, RequestContext(request))
class restauranteCardapioNovoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-novo.html', {}, RequestContext(request))
class restauranteCardapioEditarView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-editar.html', {}, RequestContext(request))
class restauranteCardapioExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-excluir.html', {}, RequestContext(request))
class restauranteCardapioCategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-categorias.html', {}, RequestContext(request))
class restauranteCardapioCategoriasNovaView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-categoria-novo.html', {}, RequestContext(request))
class restauranteCardapioCategoriasExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-cardapio-categoria-excluir.html', {}, RequestContext(request))
class restauranteRepasseView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-repasse.html', {}, RequestContext(request))
class restaurantePedidosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-pedidos.html', {}, RequestContext(request))
class restauranteAvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-avaliacoes.html', {}, RequestContext(request))
class restauranteAtendimentoNovoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-atendimento-novo.html', {}, RequestContext(request))
class restauranteAtendimentoExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('restaurante/restaurante-atendimento-excluir.html', {}, RequestContext(request))

class clienteHomeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-home.html', {}, RequestContext(request))
class clientePerfilView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-perfil.html', {}, RequestContext(request))
class clientePedidosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-pedidos.html', {}, RequestContext(request))
class clienteRestauranteView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-restaurante-integra.html', {}, RequestContext(request))
class clienteProdutoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-produto-integra.html', {}, RequestContext(request))
class clienteRealizarPedidoEnderecoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-realizar-pedido-endereco.html', {}, RequestContext(request))
class clienteRealizarPedidoTipoPagamentoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-realizar-pedido-tipo-pagamento.html', {}, RequestContext(request))
class clienteRealizarPedidoPagamentoNaEntregaView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-realizar-pedido-pagamento-naentrega.html', {}, RequestContext(request))
class clienteRealizarPedidoPagamentoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-realizar-pedido-pagamento.html', {}, RequestContext(request))
class clientePedidoIntegraView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-pedido-integra.html', {}, RequestContext(request))
class clienteAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('cliente/cliente-avaliacao.html', {}, RequestContext(request))




class adminLoginView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/login.html', {}, RequestContext(request))
class adminHomeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/home.html', {}, RequestContext(request))

class adminCategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/categoria/categorias.html', {}, RequestContext(request))
class adminCategoriaNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/categoria/novo.html', {}, RequestContext(request))
class adminCategoriaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/categoria/editar.html', {}, RequestContext(request))
class adminCategoriaExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/categoria/excluir.html', {}, RequestContext(request))
class adminCategoriaVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/categoria/ver.html', {}, RequestContext(request))

class adminClientesView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/cliente/clientes.html', {}, RequestContext(request))
class adminClienteNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/cliente/novo.html', {}, RequestContext(request))
class adminClienteEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/cliente/editar.html', {}, RequestContext(request))
class adminClienteExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/cliente/excluir.html', {}, RequestContext(request))
class adminClienteVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/cliente/ver.html', {}, RequestContext(request))
class adminClienteRecuperarSenha(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/cliente/esqueceusenha.html', {}, RequestContext(request))

class adminSubCategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/subcategoria/subcategorias.html', {}, RequestContext(request))
class adminSubCategoriaNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/subcategoria/novo.html', {}, RequestContext(request))
class adminSubCategoriaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/subcategoria/editar.html', {}, RequestContext(request))
class adminSubCategoriaExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/subcategoria/excluir.html', {}, RequestContext(request))
class adminSubCategoriaVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/subcategoria/ver.html', {}, RequestContext(request))

class adminEmpresasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/empresa/empresas.html', {}, RequestContext(request))
class adminEmpresaNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/empresa/novo.html', {}, RequestContext(request))
class adminEmpresaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/empresa/editar.html', {}, RequestContext(request))
class adminEmpresaExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/empresa/excluir.html', {}, RequestContext(request))
class adminEmpresaVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/empresa/ver.html', {}, RequestContext(request))

class adminFuncionariosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/funcionario/funcionarios.html', {}, RequestContext(request))
class adminFuncionarioNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/funcionario/novo.html', {}, RequestContext(request))
class adminFuncionarioEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/funcionario/editar.html', {}, RequestContext(request))
class adminFuncionarioExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/funcionario/excluir.html', {}, RequestContext(request))
class adminFuncionarioVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/funcionario/ver.html', {}, RequestContext(request))

class adminOpcionaisView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/opcional/opcionais.html', {}, RequestContext(request))
class adminOpcionalNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/opcional/novo.html', {}, RequestContext(request))
class adminOpcionalEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/opcional/editar.html', {}, RequestContext(request))
class adminOpcionalExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/opcional/excluir.html', {}, RequestContext(request))
class adminOpcionalVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/opcional/ver.html', {}, RequestContext(request))

class adminOpcaoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/opcionalopcoes/opcoes.html', {}, RequestContext(request))
class adminOpcaoNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/opcionalopcoes/novo.html', {}, RequestContext(request))
class adminOpcaoExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/opcionalopcoes/excluir.html', {}, RequestContext(request))


class adminAtendimentosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/atendimento/atendimentos.html', {}, RequestContext(request))
class adminAtendimentoNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/atendimento/novo.html', {}, RequestContext(request))
class adminAtendimentoExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/atendimento/excluir.html', {}, RequestContext(request))

class adminProdutosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produto/produtos.html', {}, RequestContext(request))
class adminProdutoNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/produto/novo.html', {}, RequestContext(request))
class adminProdutoEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/produto/editar.html', {}, RequestContext(request))
class adminProdutoExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produto/excluir.html', {}, RequestContext(request))
class adminProdutoVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produto/ver.html', {}, RequestContext(request))
# class adminProdutoGaleriaView(View):
#     def get(self, request, *args, **kwargs):
#         return render_to_response('adm/galeria/fotos.html', {}, RequestContext(request))

class adminProdutoCategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/subcategorias.html', {}, RequestContext(request))
class adminProdutoCategoriasExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/excluir.html', {}, RequestContext(request))
class adminProdutoCategoriasNovoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/novo.html', {}, RequestContext(request))

class adminProdutoOpcionaisView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtoopcionais/produtoopcionais.html', {}, RequestContext(request))
class adminProdutoOpcionaisExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtoopcionais/excluir.html', {}, RequestContext(request))
class adminProdutoOpcionaisNovoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtoopcionais/novo.html', {}, RequestContext(request))

class adminPedidosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/pedido/pedidos.html', {}, RequestContext(request))
class adminPedidoNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/pedido/novo.html', {}, RequestContext(request))
class adminPedidoExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/pedido/excluir.html', {}, RequestContext(request))
class adminPedidoVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/pedido/ver.html', {}, RequestContext(request))

class adminTiposCozinhaView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/tiposcozinha/tiposcozinha.html', {}, RequestContext(request))
class adminTipoCozinhaNovaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/tiposcozinha/novo.html', {}, RequestContext(request))
class adminTipoCozinhaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adm/tiposcozinha/editar.html', {}, RequestContext(request))
class adminTipoCozinhaExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/tiposcozinha/excluir.html', {}, RequestContext(request))
class adminTipoCozinhaVerView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/tiposcozinha/ver.html', {}, RequestContext(request))

class adminRepassesAtualView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/repasse/repasseatual.html', {}, RequestContext(request))
class adminRepassesView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/repasse/repasses.html', {}, RequestContext(request))
class adminRepassesPagamentosView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/repasse/pagamentos.html', {}, RequestContext(request))
class adminCriarRepasseView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/repasse/criar.html', {}, RequestContext(request))
class adminLimitarEmpresaView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/repasse/limitar.html', {}, RequestContext(request))

class adminMensalidadesView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/mensalidade/mensalidades.html', {}, RequestContext(request))

class ServiceJson(View):

    @staticmethod
    def opcoes(request):
        # Query Base
        query = Opcao.objects.all().order_by("titulo")

        # Filtros
        titulo = request.GET.get("titulo")
        id = request.GET.get("id")
        opcional_id = request.GET.get("empresa_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (titulo):
            query = query.filter(titulo__icontains=titulo)
        if (id > 0):
            query = query.filter(id=id)
        if (opcional_id):
            query = query.filter(opcional__id=opcional_id)


        rows = []

        for op in query:
            r = {
                "id":op.id,
                "opcional__id" : op.id,
                "opcional_titulo" : op.titulo,
                "titulo":op.titulo,
                "valor":op.valor
            }

            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def opcionais(request):
        # Query Base
        query = Opcional.objects.all().order_by("titulo")

        # Filtros
        titulo = request.GET.get("titulo")
        id = request.GET.get("id")
        empresa_id = request.GET.get("empresa_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (titulo):
            query = query.filter(titulo__icontains=titulo)
        if (id > 0):
            query = query.filter(id=id)
        if (empresa_id):
            query = query.filter(empresa__id=empresa_id)


        rows = []

        for op in query:

            ops = []
            for opcao in op.Opcoes.all():
                os = {
                    "id":opcao.id,
                    "titulo":opcao.titulo,
                    "valor":opcao.valor
                }
                ops.append(os)

            r = {
                "id":op.id,
                "empresa_id" : op.empresa.id,
                "empresa_nome" : op.empresa.nome,
                "titulo":op.titulo,
                "tipo":op.tipo,
                "quantidade":op.quantidade,
                "opcoes":ops
            }

            rows.append(r)

            lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveopcao(request):
        # Filtros
        id = request.POST.get("id")
        titulo = request.POST.get("titulo")
        opcional_id = request.POST.get("opcional_id")
        valor = request.POST.get("valor")

        # Objeto de Opcional
        oOpcao = Opcao()

        if (id):
            if (int(id) > 0):
                oOpcao = Opcional.objects.get(id=id)

        oOpcao.titulo = titulo

        if opcional_id:
            if opcional_id != '?':
                oOpcional = Opcional.objects.filter(id=opcional_id).first()
                oOpcao.opcional = oOpcional

        if valor:
            oOpcao.valor = valor
        else:
            oOpcao.valor = 0

        oOpcao.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveopcional(request):
        # Filtros
        id = request.POST.get("id")
        titulo = request.POST.get("titulo")
        tipo = request.POST.get("tipo")
        empresa_id = request.POST.get("empresa_id")
        quantidade = request.POST.get("quantidade")

        # Objeto de Opcional
        oOpcional = Opcional()

        if (id):
            if (int(id) > 0):
                oOpcional = Opcional.objects.get(id=id)

        oOpcional.titulo = titulo

        if quantidade:
            oOpcional.quantidade = quantidade

        oOpcional.tipo = tipo

        if empresa_id:
            if empresa_id != '?':
                oempresa = Empresa.objects.filter(id=empresa_id).first()
                oOpcional.empresa = oempresa

        oOpcional.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluiropcional(request):
        id = request.GET.get("id")

        # Query Base
        oOpcional = Opcional.objects.filter(id=id).first()

        oOpcional.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluiropcao(request):
        id = request.GET.get("id")

        # Query Base
        oOpcao = Opcao.objects.filter(id=id).first()

        oOpcao.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def categorias(request):
        # Query Base
        query = Categoria.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome"])
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savecategoria(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")

        # Objeto de Categoria
        oCategoria = Categoria()

        if (id):
            if (int(id) > 0):
                oCategoria = Categoria.objects.get(id=id)

        oCategoria.nome = nome

        oCategoria.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveavaliacao(request):
        # Filtros
        pedido_id = request.POST.get("pedido_id")
        nota = request.POST.get("nota")
        mensagem = request.POST.get("mensagem")

        # Objeto de Avaliacao
        oAvaliacao = Avaliacao()

        oPedido = Pedido.objects.filter(id=pedido_id).first()
        oPedido.status = "Avaliado"

        oEmpresa = oPedido.empresa
        oPedido.save()

        oEmpresa.nota = oEmpresa.nota + int(nota)
        oEmpresa.ttl_avaliacoes = oEmpresa.ttl_avaliacoes + 1
        oEmpresa.nota_atual = oEmpresa.nota/oEmpresa.ttl_avaliacoes
        oEmpresa.save()

        oAvaliacao.nota = nota
        oAvaliacao.pedido = oPedido
        oAvaliacao.mensagem = mensagem

        oAvaliacao.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluircategoria(request):
        id = request.GET.get("id")

        # Query Base
        oCategoria = Categoria.objects.filter(id=id).first()

        oCategoria.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def tiposcozinhas(request):
        # Query Base
        query = TipoCozinha.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def tipostempo(request):
        # Query Base
        query = TipoTempo.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savetipocozinha(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")

        # Objeto de Tipo Cozinha
        oTipoCozinha = TipoCozinha()

        if (id):

            if(id == 'undefined'):
                id=0

            if (int(id) > 0):
                oTipoCozinha = TipoCozinha.objects.get(id=id)

        oTipoCozinha.nome = nome
        oTipoCozinha.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirtipocozinha(request):
        id = request.GET.get("id")

        # Query Base
        oTipoCozinha = TipoCozinha.objects.filter(id=id).first()

        oTipoCozinha.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def clienteLogado(request):
        # Query Base
        query = Cliente.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        email = request.GET.get("email")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (email):
            query = query.filter(email__icontains=email)

        rows = []
        if id > 0:
            for cliente in query:
                ocidade = Cidade()
                oestado = Estado()
                if cliente.cidade:
                    ocidade = cliente.cidade
                    oestado = cliente.cidade.estado

                obairro = Bairro()
                if cliente.bairro:
                    obairro = cliente.bairro



                r = {
                    "id":cliente.id,
                    "nome":cliente.nome,
                    "email":cliente.email,
                    "telefone":cliente.telefone,
                    "endereco":cliente.endereco,
                    "cidade":ocidade.nome,
                    "cidade_id":ocidade.id,
                    "bairro":obairro.nome,
                    "bairro_id":obairro.id,
                    "estado":oestado.nome,
                    "estado_id":oestado.id,
                    "complemento": cliente.complemento,
                    "numero": cliente.numero,
                    "cep": cliente.cep
                }
                rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def clientes(request):
        # Query Base
        query = Cliente.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        email = request.GET.get("email")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (email):
            query = query.filter(email__icontains=email)

        rows = []

        for cliente in query:
            ocidade = Cidade()
            oestado = Estado()
            if cliente.cidade:
                ocidade = cliente.cidade
                oestado = cliente.cidade.estado

            obairro = Bairro()
            if cliente.bairro:
                obairro = cliente.bairro



            r = {
                "id":cliente.id,
                "nome":cliente.nome,
                "email":cliente.email,
                "telefone":cliente.telefone,
                "endereco":cliente.endereco,
                "cidade":ocidade.nome,
                "cidade_id":ocidade.id,
                "bairro":obairro.nome,
                "bairro_id":obairro.id,
                "estado":oestado.nome,
                "estado_id":oestado.id,
                "complemento": cliente.complemento,
                "numero": cliente.numero,
                "cep": cliente.cep
            }
            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def clienteLogin(request):
        # Filtros
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        query = Cliente.objects.filter(email=email, senha=senha).first()
        rows = []

        if query:

            cliente = query

            cidade_nome = ''
            cidade_id = None
            bairro_nome = ''
            bairro_id = None
            estado_nome = ''
            estado_id = None

            if cliente.cidade:
                cidade_nome = cliente.cidade.nome
                cidade_id = cliente.cidade.id
                bairro_nome = cliente.bairro.nome
                bairro_id = cliente.bairro.id
                estado_nome = cliente.cidade.estado.nome
                estado_id = cliente.cidade.estado.id

            r = {
                "id":cliente.id,
                "nome":cliente.nome,
                "email":cliente.email,
                "telefone":cliente.telefone,
                "endereco":cliente.endereco,
                "cidade":cidade_nome,
                "cidade_id":cidade_id,
                "bairro":bairro_nome,
                "bairro_id":bairro_id,
                "estado":estado_nome,
                "estado_id":estado_id,
                "complemento":cliente.complemento,
                "numero":cliente.numero,
                "cep":cliente.cep
            }

            rows.append(r)
        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def clienteFaceLogin(request):
        # Filtros
        nome = request.POST.get("nome")
        face_id = request.POST.get("face_id")

        query = Cliente.objects.filter(face_id=face_id).first()



        if not query:
            oUsuario = Cliente()
            oUsuario.nome = nome
            oUsuario.face_id = face_id
            oUsuario.save()

        query = Cliente.objects.filter(face_id=face_id).first()

        rows = []

        if query:
            cliente = query

            ocidade = Cidade()
            oestado = Estado()
            if cliente.cidade:
                ocidade = cliente.cidade
                oestado = cliente.cidade.estado

            obairro = Bairro()
            if cliente.bairro:
                obairro = cliente.bairro

            r = {
                "id":cliente.id,
                "nome":cliente.nome,
                "email":cliente.email,
                "telefone":cliente.telefone,
                "endereco":cliente.endereco,
                "cidade":ocidade.nome,
                "cidade_id":ocidade.id,
                "bairro":obairro.nome,
                "bairro_id":obairro.id,
                "estado":oestado.nome,
                "estado_id":oestado.id,
                "complemento": cliente.complemento,
                "numero": cliente.numero,
                "cep": cliente.cep
            }

            rows.append(r)

        # "cidade":cliente.cidade.nome,
        # "cidade_id":cliente.cidade.id,
        # "bairro":cliente.bairro.nome,
        # "bairro_id":cliente.bairro.id,
        # "estado":cliente.cidade.estado.nome,
        # "estado_id":cliente.cidade.estado.id,
        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savecliente(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        bairro_id = request.POST.get("bairro")
        cidade_id = request.POST.get("cidade")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento")
        cep = request.POST.get("cep")

        # Objeto de Clientes
        oCliente = Cliente()

        if (id == 'undefined'):
            id = 0

        if (id):
            if not (id == 'null'):
                if (int(id) > 0):
                    oCliente = Cliente.objects.get(id=id)

        if(nome):
            oCliente.nome = nome
        if(email):
            oCliente.email = email
        if(senha):
            oCliente.senha = senha
        if(telefone):
            oCliente.telefone = telefone
        if(endereco):
            oCliente.endereco = endereco
        if(numero):
            oCliente.numero = numero
        if(complemento):
            oCliente.complemento = complemento
        if(cep):
            oCliente.cep = cep
        if(bairro_id):
            if not (bairro_id == '?'):
                oCliente.bairro = Bairro.objects.filter(id=bairro_id).first()
        if(cidade_id):
            if not (cidade_id == '?'):
                oCliente.cidade = Cidade.objects.filter(id=cidade_id).first()

        oCliente.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveclientehome(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        bairro_id = request.POST.get("bairro")
        cidade_id = request.POST.get("cidade")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento")
        cep = request.POST.get("cep")

        # Objeto de Clientes
        oCliente = Cliente()

        if (id == 'undefined'):
            id = 0

        if (id):
            if not (id == 'null'):
                if (int(id) > 0):
                    oCliente = Cliente.objects.get(id=id)

        if(nome):
            oCliente.nome = nome
        if(email):
            oCliente.email = email
        if(senha):
            oCliente.senha = senha
        if(telefone):
            oCliente.telefone = telefone
        if(endereco):
            oCliente.endereco = endereco
        if(numero):
            oCliente.numero = numero
        if(complemento):
            oCliente.complemento = complemento
        if(cep):
            oCliente.cep = cep
        if(bairro_id):
            if not (bairro_id == '?'):
                oCliente.bairro = Bairro.objects.filter(id=bairro_id).first()
        if(cidade_id):
            if not (cidade_id == '?'):
                oCliente.cidade = Cidade.objects.filter(id=cidade_id).first()

        oCliente.save()

        lista = oCliente.id
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluircliente(request):
        id = request.GET.get("id")

        # Query Base
        oCliente = Cliente.objects.filter(id=id).first()

        oCliente.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def subcategorias(request):
        # Query Base
        query = SubCategoria.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        categoria_id = request.GET.get("categoria")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (categoria_id):
            query = query.filter(categoria__id=categoria_id)
        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome", "categoria__id", "categoria__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savesubcategoria(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        categoria_id = request.POST.get("categoria")

        # Objeto de SubCategoria
        oSubcategoria = SubCategoria()

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (id):
            if (int(id) > 0):
                oSubcategoria = SubCategoria.objects.get(id=id)

        oSubcategoria.nome = nome

        if(categoria_id):
            oSubcategoria.categoria = Categoria.objects.filter(id=categoria_id).first()

        oSubcategoria.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirsubcategoria(request):
        id = request.GET.get("id")

        # Query Base
        oSubcategoria = SubCategoria.objects.filter(id=id).first()

        oSubcategoria.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def estados(request):
        # Query Base
        query = Estado.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (id == None):
            id = 0

        id = int(id)

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveestado(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")

        # Objeto de Estados
        oEstado = Estado()

        if (id):
            if (int(id) > 0):
                oEstado = Estado.objects.get(id=id)

        oEstado.nome = nome

        oEstado.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def cidades(request):
        # Query Base
        query = Cidade.objects.all().order_by("nome")

        # Filtros
        estado_id = request.GET.get("estado_id")
        nome = request.GET.get("nome")
        id = request.GET.get("id")


        if (estado_id):
            query = query.filter(estado__id=estado_id)
        if (id == None):
            id = 0

        id = int(id)

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)


        lista = serialize('json', query, fields=["id", "nome", "estado__id", "estado__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savecidade(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        estado_id = request.POST.get("estado_id")

        # Objeto de Cidades
        oCidade = Cidade()

        if (id):
            if (int(id) > 0):
                oCidade = Cidade.objects.get(id=id)

        oCidade.nome = nome
        oCidade.estado = Estado.objects.filter(id=estado_id).first()

        oCidade.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def bairros(request):
        # Query Base
        query = Bairro.objects.all().order_by("nome")

        # Filtros
        cidade_id = request.GET.get("cidade_id")
        nome = request.GET.get("nome")
        id = request.GET.get("id")

        if (cidade_id):
            query = query.filter(cidade__id=cidade_id)
        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0
        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)

        lista = serialize('json', query, fields=["id", "nome", "cidade__id", "cidade__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savebairro(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        cidade_id = request.POST.get("estado_id")

        # Objeto de Bairros
        oBairro = Bairro()

        if (id):
            if (int(id) > 0):
                oBairro = Bairro.objects.get(id=id)

        oBairro.nome = nome
        oBairro.cidade = Estado.objects.filter(id=cidade_id).first()

        oBairro.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def empresas(request):
        # Query Base
        query = Empresa.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        email = request.GET.get("email")
        lista_bairros = request.GET.get("bairros")

        if (id == None):
            id = 0

        id = int(id)

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (email):
            query = query.filter(email__icontains=email)
        if (lista_bairros):
            bairros = lista_bairros.split(",")
            query = query.filter(bairros__id__in=bairros)

        rows = []

        for empresa in query:

            bairros = []
            avaliacoes = []

            lista_avaliacoes = Avaliacao.objects.filter(pedido__empresa__id=empresa.id).order_by("-data")

            for avaliacao in lista_avaliacoes:
                r_avaliacao = {
                    "avaliacao_id":avaliacao.id,
                    "avaliacao_nota":avaliacao.nota,
                    "avaliacao_mensagem":avaliacao.mensagem,
                    "avaliacao_data":avaliacao.data.strftime('%d-%m-%Y'),
                    "avaliador":avaliacao.pedido.cliente.nome
                }

                avaliacoes.append(r_avaliacao)

            otipotempo = TipoTempo()
            if empresa.tempo:
                otipotempo = empresa.tempo

            for bairro_at in empresa.BairrosAtendimento.all():
                r_bairro = {
                    "bairro":bairro_at.bairro.nome,
                    "bairro_id":bairro_at.bairro.id,
                    "frete":bairro_at.frete
                }

                bairros.append(r_bairro)

            r = {
                "id": empresa.id,
                "nome": empresa.nome,
                "email": empresa.email,
                "telefone": empresa.telefone,
                "endereco": empresa.endereco,
                "cidade": empresa.cidade.nome,
                "cidade_id": empresa.cidade.id,
                "estado": empresa.cidade.estado.nome,
                "estado_id": empresa.cidade.estado.id,
                "bairro":empresa.bairro.nome,
                "bairro_id":empresa.bairro.id,
                "bairros":bairros,
                "descricao":empresa.descricao,
                "tipo_cozinha":empresa.tipocozinha.nome,
                "tipo_cozinha_id":empresa.tipocozinha.id,
                "tipo_tempo":otipotempo.nome,
                "tipo_tempo_id":otipotempo.id,
                "avaliacoes":avaliacoes,
                "aceita_cartao":empresa.aceita_cartao,
                "aceita_valerefeicao":empresa.aceita_valerefeicao,
                "aceita_pagamentoonline":empresa.aceita_pagamentoonline,
                "porcentagem_repasse":empresa.porcentagem_repasse,
                "valor_mensalidade":empresa.valor_mensalidade,
                "logotipo":empresa.logotipo,
                "numero":empresa.numero,
                "cep":empresa.cep,
                "complemento":empresa.complemento

            }

            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def empresasrepasses(request):
        # Query Base
        query = Empresa.objects.all().order_by("nome")

        nome = request.GET.get("nome")
        id = request.GET.get("id")
        email = request.GET.get("email")
        data = request.GET.get("data_fim")
        data_final = datetime.now()
        lista_bairros = request.GET.get("bairros")

        if data:
            data_final = data

        if (id == None):
            id = 0

        id = int(id)

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (email):
            query = query.filter(email__icontains=email)
        if (lista_bairros):
            bairros = lista_bairros.split(",")
            query = query.filter(bairros__id__in=bairros)

        rows = []

        for empresa in query:

            bairros = []
            avaliacoes = []
            repasses = []
            pagamentos = []
            total_mercadopago = 0
            qtd_mercadopago = 0
            total_naentrega=0
            qtd_naentrega=0
            ultima_data = datetime.now()

            lista_avaliacoes = Avaliacao.objects.filter(pedido__empresa__id=empresa.id).order_by("-data")
            lista_repasses = empresa.Repasses.all().order_by("-data_inicio")
            lista_pagamentos = Pagamento.objects.filter(pedido__empresa__id=empresa.id,pedido__data__lte=data_final).order_by("id")


            if(len(lista_repasses) > 0):
                lista_pagamentos = lista_pagamentos.filter(pedido__data__gt=lista_repasses[0].data_fim)
                ultima_data = lista_repasses[0].data_fim
            else:
                if(len(lista_pagamentos) > 0):
                    ultima_data = lista_pagamentos[0].pedido.data

            for pag in lista_pagamentos:
                if "na_entrega" in pag.tipopagamento:
                    total_naentrega = total_naentrega + pag.total
                    qtd_naentrega = qtd_naentrega + 1
                else:
                    total_mercadopago = total_mercadopago + pag.total
                    qtd_mercadopago =qtd_mercadopago +1

                r_pagamento = {
                    "id":pag.id,
                    "total":pag.total,
                    "data":pag.pedido.data.strftime('%Y-%m-%d %H:%M'),
                    "tipopagamento":pag.tipopagamento,
                    "obs":pag.obs
                }
                pagamentos.append(r_pagamento)

            for avaliacao in lista_avaliacoes:
                r_avaliacao = {
                    "avaliacao_id":avaliacao.id,
                    "avaliacao_nota":avaliacao.nota,
                    "avaliacao_mensagem":avaliacao.mensagem,
                    "avaliacao_data":avaliacao.data.strftime('%d-%m-%Y'),
                    "avaliador":avaliacao.pedido.cliente.nome
                }
                avaliacoes.append(r_avaliacao)

            for bairro_at in empresa.BairrosAtendimento.all():
                r_bairro = {
                    "bairro":bairro_at.bairro.nome,
                    "bairro_id":bairro_at.bairro.id,
                    "frete":bairro_at.frete
                }
                bairros.append(r_bairro)


            for repasse in lista_repasses:
                r_repasse = {
                    "id":repasse.id,
                    "referencia":repasse.referencia,
                    "data_inicio":repasse.data_inicio.strftime('%Y-%m-%d %H:%M'),
                    "data_fim":repasse.data_fim.strftime('%Y-%m-%d %H:%M'),
                    "total":repasse.total,
                    "pago":repasse.pago
                }
                repasses.append(r_repasse)


            r = {
                "id": empresa.id,
                "nome": empresa.nome,
                "email": empresa.email,
                "telefone": empresa.telefone,
                "endereco": empresa.endereco,
                "cidade": empresa.cidade.nome,
                "cidade_id": empresa.cidade.id,
                "estado": empresa.cidade.estado.nome,
                "estado_id": empresa.cidade.estado.id,
                "bairro":empresa.bairro.nome,
                "bairro_id":empresa.bairro.id,
                "bairros":bairros,
                "descricao":empresa.descricao,
                "tipo_cozinha":empresa.tipocozinha.nome,
                "tipo_cozinha_id":empresa.tipocozinha.id,
                "avaliacoes":avaliacoes,
                "aceita_cartao":empresa.aceita_cartao,
                "aceita_valerefeicao":empresa.aceita_valerefeicao,
                "aceita_pagamentoonline":empresa.aceita_pagamentoonline,
                "repasses":repasses,
                "total_mercadopago":total_mercadopago,
                "qtd_mercadopago":qtd_mercadopago,
                "total_naentrega":total_naentrega,
                "qtd_naentrega":qtd_naentrega,
                "total":((total_naentrega+total_mercadopago) * (float(empresa.porcentagem_repasse)/float(100))) - total_mercadopago,
                "status":empresa.status,
                "ultima_data":ultima_data.strftime('%Y-%m-%d'),
                "pagamentos":pagamentos,
                "porcentagem_repasse":empresa.porcentagem_repasse,
                "referencia":str(empresa.id) + "_" + str(ultima_data.strftime('%Y%m%d')) + "_",
                "logotipo":empresa.logotipo,
                "numero": empresa.numero,
                "cep": empresa.cep,
                "complemento": empresa.complemento
            }

            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def empresaslogotipos(request):
        # Query Base
        query = Empresa.objects.all().order_by("-id")[:5]

        rows = []

        for empresa in query:
            r = {
                "id": empresa.id,
                "nome": empresa.nome,
                "logotipo":empresa.logotipo
            }

            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def empresasavaliacoes(request):
        # Query Base
        query = Avaliacao.objects.exclude(mensagem="").order_by("-id")[:4]

        rows = []

        for avaliacao in query:
            r = {
                "id": avaliacao.id,
                "mensagem": avaliacao.mensagem,
                "data":avaliacao.data.strftime('%Y-%m-%d'),
                "cliente":avaliacao.pedido.cliente.nome,
                "empresa":avaliacao.pedido.empresa.nome
            }

            rows.append(r)

        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveempresa(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        cidade_id = request.POST.get("cidade")
        estado_id = request.POST.get("estado")
        bairro_id = request.POST.get("bairro")
        endereco = request.POST.get("endereco")
        tipocozinha_id = request.POST.get("tipo_cozinha_id")
        aceita_cartao = request.POST.get("aceita_cartao")
        aceita_valerefeicao = request.POST.get("aceita_valerefeicao")
        aceita_pagamentoonline = request.POST.get("aceita_pagamentoonline")
        porcentagem_repasse = request.POST.get("porcentagem_repasse")
        valor_mensalidade = request.POST.get("valor_mensalidade")
        random_n = random.randint(1, 500000000)
        foto = request.POST.get("logotipo")
        cep = request.POST.get("cep")
        complemento = request.POST.get("complemento")
        numero = request.POST.get("numero")

        print id
        print cidade_id
        print estado_id
        print bairro_id
        print tipocozinha_id
        print foto


        # Objeto de Empresas
        oEmpresa = Empresa()

        if (id):
            if (int(id) > 0):
                oEmpresa = Empresa.objects.get(id=id)

        if nome:
            oEmpresa.nome = nome

        if descricao:
            oEmpresa.descricao = descricao

        if email:
            oEmpresa.email = email

        if senha:
            oEmpresa.senha = senha

        if telefone:
            oEmpresa.telefone = telefone

        if porcentagem_repasse:
            oEmpresa.porcentagem_repasse = porcentagem_repasse

        if not cidade_id == '?':
            if cidade_id:
                oEmpresa.cidade = Cidade.objects.filter(id=cidade_id).first()

        if not estado_id == '?':
            if estado_id:
                oEmpresa.estado = Estado.objects.filter(id=estado_id).first()

        if not bairro_id == '?':
            if bairro_id:
                oEmpresa.bairro = Bairro.objects.filter(id=bairro_id).first()

        if not tipocozinha_id == '?':
            if tipocozinha_id:
                oEmpresa.tipocozinha = TipoCozinha.objects.filter(id=tipocozinha_id).first()

        if endereco:
            oEmpresa.endereco=endereco

        if valor_mensalidade:
            oEmpresa.valor_mensalidade = valor_mensalidade

        if aceita_cartao != 'undefined':
            oEmpresa.aceita_cartao=True
        else:
            oEmpresa.aceita_cartao = False

        if aceita_valerefeicao != 'undefined':
            oEmpresa.aceita_valerefeicao=True
        else:
            oEmpresa.aceita_valerefeicao=False

        if aceita_pagamentoonline != 'undefined':
            oEmpresa.aceita_pagamentoonline=True
        else:
            oEmpresa.aceita_pagamentoonline=False

        if numero:
            oEmpresa.numero = numero
        if complemento:
            oEmpresa.complemento = complemento
        if cep:
            oEmpresa.cep = cep

        oEmpresa.save()

        print foto

        if not foto == '123':
            filename = str(oEmpresa.id) + '_' + str(random_n) + '.jpg'
            image_data = open(settings.BASE_DIR + '/game7api/static/media/empresa/' + filename, "wb")
            image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
            image_data.close()

            oEmpresa.logotipo = filename
            oEmpresa.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def enviarempresa(request):
        # Filtros
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        responsavel = request.POST.get("responsavel")
        estado_id = request.POST.get("estado")
        cidade_id = request.POST.get("cidade")
        bairro_id = request.POST.get("bairro")
        endereco = request.POST.get("endereco")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento")
        cep = request.POST.get("cep")
        tipocozinha_id = request.POST.get("tipo_cozinha_id")


        oEstado = Estado.objects.filter(id=estado_id).first()
        oCidade = Cidade.objects.filter(id=cidade_id).first()
        oBairro = Bairro.objects.filter(id=bairro_id).first()
        oTipoCozinha = TipoCozinha.objects.filter(id=tipocozinha_id).first()

        CorpoEmail = smart_str("""
                        <html>
                            <head>
                                <title>Menuweb - Notificacao de Recebimento de Pre Cadastro</title>
                            </head>
                            <body>
                                Ola <b>MenuWeb</b>, <br/>
                                recebemos um novo cadastro do restaurante <b>{}</b> que e do tipo <b>{}</b>.
                                O mesmo fica na {}, {}, {}, {} - {} - {} - {} <br/><br/>

                                Fale com o {} pelo telefone {} ou pelo email {}. <br/><br/>

                                Equipe MenuWeb.
                            </body>
                        </html>
                    """)

        CorpoEmail = CorpoEmail.format(smart_str(nome), smart_str(oTipoCozinha.nome), smart_str(endereco), smart_str(numero), smart_str(oBairro.nome), smart_str(complemento), smart_str(oCidade.nome), smart_str(oEstado.nome), smart_str(cep), smart_str(responsavel), smart_str(telefone), smart_str(email))


        message = Message(From="noreplay@menuweb.com.br", To="luk14236@gmail.com")
        message.Subject = "Menuweb - Notificacao de pre cadastro de restaurante"
        message.Html = CorpoEmail

        smtp = Mailer(host='smtp.gmail.com', port=587, usr='menuwebapi@gmail.com', pwd='api2017@app', use_tls=True)
        smtp.send(message)

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def criarrepasse(request):

        # Populando as variaveis
        ultima_data = datetime.now()
        total_mercadopago = 0
        total_naentrega = 0

        # Filtros
        id = request.POST.get("id")
        ref = request.POST.get("referencia")
        data_final = request.POST.get("data_final")
        status_parametro = request.POST.get("status")
        status = False

        # Populando a Empresa
        if not (data_final):
            data_final = datetime.now()

        oempresa = Empresa.objects.filter(id=id).first()
        lista_repasses = oempresa.Repasses.all().order_by("-data_inicio")
        lista_pagamentos = Pagamento.objects.filter(pedido__empresa__id=oempresa.id, pedido__data__lte=data_final).order_by("id")

        # Populando a ultima data de repasse
        if (len(lista_repasses) > 0):
            lista_pagamentos = lista_pagamentos.filter(pedido__data__gt=lista_repasses[0].data_fim)
            ultima_data = lista_repasses[0].data_fim
        else:
            if(len(lista_pagamentos) > 0):
                ultima_data = lista_pagamentos[0].pedido.data

        # Atualizando os totais
        for pag in lista_pagamentos:
            if "na_entrega" in pag.tipopagamento:
                total_naentrega = total_naentrega + pag.total
            else:
                total_mercadopago = total_mercadopago + pag.total

        # Montando o Repasse
        orepasse = Repasse()
        orepasse.referencia = ref
        orepasse.data_inicio = ultima_data
        orepasse.data_fim = data_final
        orepasse.total = total_mercadopago+total_naentrega
        orepasse.empresa = oempresa

        if status_parametro == 'true':
            status = True
            orepasse.data_pagamento = datetime.now()
        else:
            orepasse.data_bloqueio = datetime.now()

        orepasse.pago = status
        orepasse.save()

        if orepasse.pago:
            status_autorizado = True
            for rep in lista_repasses:
                if not rep.pago:
                    status_autorizado = False

            if status_autorizado:
                oempresa.status = "ok"
            else:
                oempresa.status = "LIMITADO"
        else:
            oempresa.status = "LIMITADO"

        oempresa.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def receberrepasse(request):
        # Variaveis
        Liberado = "OK"

        # Filtros
        id = request.POST.get("id")

        # Montando o Repasse
        orepasse = Repasse.objects.filter(id=id).first()
        orepasse.pago = True
        orepasse.save()

        oempresa = orepasse.empresa

        for rep in oempresa.Repasses.all():
            if not rep.pago:
                Liberado = "LIMITADO"

        oempresa.status = Liberado
        oempresa.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirempresa(request):
        id = request.GET.get("id")

        # Query Base
        oEmpresa = Empresa.objects.filter(id=id).first()
        oEmpresa.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def empresaLogin(request):
        # Filtros
        email = request.POST.get("email")
        senha = request.POST.get("senha")


        empresa = Empresa.objects.filter(email=email, senha=senha).first()
        rows = []
        r = []

        if empresa:
            for bairro_at in empresa.BairrosAtendimento.all():
                r_bairro ={
                    "bairro":bairro_at.bairro.nome,
                    "bairro_id":bairro_at.bairro.id,
                    "frete":bairro_at.frete
                }

                rows.append(r_bairro)
            r = {
                "id":empresa.id,
                "nome":empresa.nome,
                "email":empresa.email,
                "descricao":empresa.descricao,
                "endereco":empresa.endereco,
                "cidade":empresa.cidade.nome,
                "cidade_id":empresa.cidade.id,
                "bairro":empresa.bairro.nome,
                "bairro_id":empresa.bairro.id,
                "estado":empresa.cidade.estado.nome,
                "estado_id":empresa.cidade.estado.id,
                "bairros_atendimento":rows,
                "aceita_cartao":empresa.aceita_cartao,
                "aceita_valerefeicao":empresa.aceita_valerefeicao,
                "aceita_pagamentoonline":empresa.aceita_pagamentoonline,
                "logotipo":empresa.logotipo,
                "numero": empresa.numero,
                "cep": empresa.cep,
                "complemento": empresa.complemento
            }

        lista = json.dumps(r)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def settempoentrega(request):
        # Filtros
        id = request.GET.get("id")
        tempo_id = request.GET.get("tempo_id")

        # Objeto de Empresa
        oEmpresa = Empresa.objects.filter(id=id).first()
        oTempo= TipoTempo.objects.filter(id=tempo_id).first()

        oEmpresa.tempo = oTempo
        oEmpresa.save()

        lista = "True"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveempresabairro(request):
        # Filtros
        id = request.POST.get("id")
        bairro_id = request.POST.get("bairro")
        frete = request.POST.get("frete")

        # Objeto de Empresa
        oEmpresa = Empresa.objects.filter(id=id).first()
        oBairro = Bairro.objects.filter(id=bairro_id).first()

        if (BairroAtendimento.objects.filter(bairro__id=bairro_id).count())==0:
            oBairroAtendimento = BairroAtendimento()
            oBairroAtendimento.empresa = oEmpresa
            oBairroAtendimento.bairro = oBairro
            oBairroAtendimento.frete = frete

            oBairroAtendimento.save()

            lista = "true"
        else:
            lista = "false"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirempresa_bairro(request):
        empresa_id = request.GET.get("empresa_id")
        bairro_id = request.GET.get("bairro_id")

        # Query Base
        oBairroAtendimento = BairroAtendimento.objects.filter(bairro__id=bairro_id,empresa__id=empresa_id).first()
        oBairroAtendimento.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def abrirempresa(request):
        id = request.GET.get("e_id")


        oAbertura = Abertura.objects.filter(empresa__id=id, fechamento__isnull=True).first()

        if not (oAbertura):
            oEmpresa = Empresa.objects.filter(id=id).first()

            oAbertura = Abertura();
            oAbertura.abertura = datetime.now()
            oAbertura.empresa = oEmpresa
            oAbertura.save()

        rows = []

        r = {
            "id": oAbertura.id,
            "abertura": oAbertura.abertura.strftime('%Y-%m-%d %H:%M'),
            "fechamento": oAbertura.fechamento
        }

        rows.append(r)
        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def fecharempresa(request):
        id = request.GET.get("id")

        # Query Base
        oAbertura = Abertura.objects.filter(id=id).first()
        oAbertura.fechamento = datetime.now()
        oAbertura.save()

        rows = []

        oAbertura = Abertura.objects.filter(empresa__id=id, fechamento__isnull=True).first()

        if (oAbertura):
            r = {
                "id": oAbertura.id,
                "abertura": oAbertura.abertura.strftime('%Y-%m-%d %H:%M'),
                "fechamento": oAbertura.fechamento.strftime('%Y-%m-%d %H:%M'),
            }
            rows.append(r)

        lista = json.dumps(rows)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def getabertura(request):
        id = request.GET.get("e_id")

        oAbertura = Abertura.objects.filter(empresa__id=id, fechamento__isnull=True).first()

        rows = []

        if (oAbertura):
            r = {
                "id": oAbertura.id,
                "abertura": oAbertura.abertura.strftime('%Y-%m-%d %H:%M'),
                "fechamento": oAbertura.fechamento
            }
            rows.append(r)

        lista = json.dumps(rows)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def getaberturas(request):
        id = request.GET.get("e_id")

        Aberturas = Abertura.objects.filter(empresa__id=id).order_by("-fechamento")

        rows = []

        for oAbertura in Aberturas:

            if oAbertura.abertura:
                s_date_abertura = oAbertura.abertura.strftime('%Y-%m-%d %H:%M')
            else:
                s_date_abertura = ''

            if oAbertura.fechamento:
                s_date_fechamento = oAbertura.fechamento.strftime('%Y-%m-%d %H:%M')
            else:
                s_date_fechamento = ''

            r = {
                "id": oAbertura.id,
                "abertura": s_date_abertura,
                "fechamento": s_date_fechamento
            }
            rows.append(r)

        lista = json.dumps(rows)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def esqueceusenhacliente(request):
        email = request.GET.get("email")

        h = hashlib.md5()
        h.update("luk1"+str(email)+"game7")

        hash_key = h.hexdigest()

        msg = """
        Ola, <br/>

        para recuperar a sua senha basta clicar na link abaixo <br/><br/>

        <a href='http://0.0.0.0:8010/adm/cliente-recuperarsenha/?key=%s'>Recupere sua senha</a> <br/><br/>
        """%(hash_key)

        message = Message(From="noreplay@menuweb.com.br", To=email)
        # message = Message(From="menuwebapi@gmail.com", To=email)
        message.Subject = "Menuweb - Esqueceu sua senha"
        message.Html = msg

        smtp = Mailer(host='smtp.gmail.com', port=587, usr='menuwebapi@gmail.com', pwd='api2017@app', use_tls=True)
        smtp.send(message)

        lista = True

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def recuperarsenhacliente(request):
        # Filtros
        token = request.POST.get("token")
        email = request.POST.get("email")
        senha = request.POST.get("senha")


        # Objeto de Cliente
        oCliente = Cliente.objects.filter(email=email).first()

        h = hashlib.md5()
        h.update("luk1"+str(email)+"game7")

        hash_key = h.hexdigest()

        if(hash_key == token):
            oCliente.senha = senha
            oCliente.save()
            lista = "true"
        else:
            lista = "false"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savefuncionario(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")

        # Objeto de Funcionarios
        oFuncionario = Funcionario()

        if (id):
            if (int(id) > 0):
                oFuncionario = Funcionario.objects.get(id=id)

        oFuncionario.nome = nome
        oFuncionario.email = email
        oFuncionario.senha = senha
        oFuncionario.telefone = telefone
        oFuncionario.endereco = endereco

        oFuncionario.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def funcionarios(request):
        # Query Base
        query = Funcionario.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("funcionario_id")
        email = request.GET.get("email")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (email):
            query = query.filter(email__icontains=email)

        lista = serialize('json', query, fields=["id", "nome", "telefone", "email", "endereco"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savefuncionario(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")

        # Objeto de Funcionarios
        oFuncionario = Funcionario()

        if (id):
            if (int(id) > 0):
                oFuncionario = Funcionario.objects.get(id=id)

        oFuncionario.nome = nome
        oFuncionario.email = email
        oFuncionario.senha = senha
        oFuncionario.telefone = telefone
        oFuncionario.endereco = endereco

        oFuncionario.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def funcionarioLogin(request):
        # Filtros
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        query = Funcionario.objects.filter(email=email, senha=senha).first()
        rows = []

        if query:
            funcionario = query
            r = {
                "id":funcionario.id,
                "nome":funcionario.nome,
                "email":funcionario.email,
                "endereco":funcionario.endereco,
                "telefone":funcionario.telefone
            }

            rows.append(r)
        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirfuncionario(request):
        id = request.GET.get("id")

        # Query Base
        oFuncionario = Funcionario.objects.filter(id=id).first()
        oFuncionario.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def repasses(request):
        # Query Base
        query = Repasse.objects.all().order_by("nome")

        # Filtros
        referencia = request.GET.get("referencia")
        id = request.GET.get("id")
        data_inicio = request.GET.get("data_inicio")
        data_fim = request.GET.get("data_fim")
        pago = request.GET.get("pago")
        empresa_id = request.GET.get("empresa_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (referencia):
            query = query.filter(referencia__icontains=referencia)
        if (id > 0):
            query = query.filter(id=id)

        if (data_inicio):
            if (data_fim):
                query = query.filter(data_inicio__gte=data_inicio, data_fim_lte=data_fim)
            else:
                query = query.filter(data_inicio__gte=data_inicio)
        else:
            raise Exception("Necessario passar a data inicio do repasse")

        if (pago):
            query = query.filter(pago=pago)

        if (empresa_id):
            query = query.filter(empresa__id=empresa_id)

        lista = serialize('json', query, fields=["id", "referencia", "data_inicio", "data_fim", "total", "pago", "empresa__id", "empresa__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saverepasse(request):
        # Filtros
        id = request.POST.get("id")
        referencia = request.POST.get("referencia")
        data_inicio = request.POST.get("data_inicio")
        data_fim = request.POST.get("data_fim")
        total = request.POST.get("total")
        pago = request.POST.get("pago")
        empresa_id = request.POST.get("empresa_id")

        # Objeto de Repasses
        oRepasse = Repasse()

        if (id):
            if (int(id) > 0):
                oRepasse = Repasse.objects.get(id=id)

        oRepasse.referencia = referencia
        oRepasse.data_inicio = data_inicio
        oRepasse.data_fim = data_fim
        oRepasse.total = total
        oRepasse.pago = pago
        oRepasse.empresa = Empresa.objects.filter(id=empresa_id)

        oRepasse.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirrepasse(request):
        id = request.GET.get("id")

        # Query Base
        oRepasse = Repasse.objects.filter(id=id).first()
        oRepasse.delete()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    # @staticmethod
    # @csrf_exempt
    # def saveprodutofoto(request):
    #     # Filtros
    #     id = request.POST.get("id")
    #     foto = request.POST.get("foto")
    #     random_n = random.randint(1, 500000000)
    #
    #     oProduto = Produto.objects.filter(id=id).first()
    #
    #     filename = str(oProduto.id) + '_' + str(random_n) + '.jpg'
    #
    #     image_data = open(settings.BASE_DIR + '/game7api/static/media/produto/' + filename, "wb")
    #     image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
    #     image_data.close()
    #
    #     oFoto = Foto()
    #     oFoto.caminho = filename
    #     oFoto.produto = oProduto
    #     oFoto.save()
    #
    #     lista = "true"
    #     return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveprodutosubcategoria(request):
        # Filtros
        id = request.POST.get("id")
        subcategoria_id = request.POST.get("subcategoria_id")

        oProduto = Produto.objects.filter(id=id).first()
        oSubcategoria = SubCategoria.objects.filter(id=subcategoria_id).first()

        oProduto.subcategorias.add(oSubcategoria)
        oProduto.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveprodutoopcional(request):
        # Filtros
        id = request.POST.get("id")
        opcional_id = request.POST.get("opcional_id")

        oProduto = Produto.objects.filter(id=id).first()
        oOpcional = Opcional.objects.filter(id=opcional_id).first()

        print oOpcional

        oProduto.opcionais.add(oOpcional)
        oProduto.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirproduto_categoria(request):
        produto_id = request.GET.get("p_id")
        subcategoria_id = request.GET.get("subc_id")

        # Query Base
        oProduto = Produto.objects.filter(id=produto_id).first()
        oSubCategoria = SubCategoria.objects.filter(id=subcategoria_id).first()

        oProduto.subcategorias.remove(oSubCategoria)
        oProduto.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirproduto_opcional(request):
        produto_id = request.GET.get("p_id")
        opcional_id = request.GET.get("op_id")

        print produto_id
        print opcional_id

        # Query Base
        oProduto = Produto.objects.filter(id=produto_id).first()
        oOpcional = Opcional.objects.filter(id=opcional_id).first()

        oProduto.opcionais.remove(oOpcional)
        oProduto.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    # @staticmethod
    # def excluirproduto_foto(request):
    #     foto_id = request.GET.get("f_id")
    #
    #     # Query Base
    #     oFoto = Foto.objects.filter(id=foto_id).first()
    #     oFoto.delete()
    #
    #     lista = "true"
    #     return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveproduto(request):
        # Filtros
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        foto = request.POST.get("foto")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        empresa_id = request.POST.get("empresa_id")
        random_n = random.randint(1,500000000)
        subcategoria_id = request.POST.get("subcategoria_id")
        lista_opcionais = request.POST.get("opcionais")

        print lista_opcionais

        # Objeto de Produtos
        oProduto = Produto()

        # print id

        if (id):
            if (id == 'undefined'):
                id = 0

            if (int(id) > 0):
                oProduto = Produto.objects.get(id=id)

        oProduto.nome=nome
        oProduto.descricao=descricao
        oProduto.preco=preco
        if empresa_id:
            if (empresa_id == '?'):
                empresa_id = 0

            if(int(empresa_id)>0):
                oProduto.empresa = Empresa.objects.filter(id=empresa_id).first()
        oProduto.save()

        print subcategoria_id

        if subcategoria_id:
            oSubCategoria = SubCategoria.objects.filter(id=subcategoria_id).first()
            oProduto.subcategorias.add(oSubCategoria)
            oProduto.save()

        try:
            filename = str(oProduto.id) + '_' + str(random_n) + '.jpg'
            image_data = open(settings.BASE_DIR + '/game7api/static/media/produto/' + filename, "wb")
            image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
            image_data.close()

            oProduto.foto = filename
            oProduto.save()
        except:
            foto = "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"
            filename = str(oProduto.id) + '_' + str(random_n) + '.jpg'
            image_data = open(settings.BASE_DIR + '/game7api/static/media/produto/' + filename, "wb")
            image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
            image_data.close()

            oProduto.foto = filename
            oProduto.save()


        #pegando a lista de opcionais

        opcionais = oProduto.opcionais.all()
        for op in opcionais:
            oProduto.opcionais.remove(op)
            oProduto.save()

        if lista_opcionais:
            opcionais = lista_opcionais.split(",")
            for op_id in opcionais:
                oOpcional = Opcional.objects.filter(id=op_id).first()

                oProduto.opcionais.add(oOpcional)
                oProduto.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirproduto(request):
        id = request.GET.get("id")

        # Query Base
        oProduto = Produto.objects.filter(id=id).first()
        oProduto.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def cardapio(request):
        # Query Base
        query = Produto.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        descricao = request.GET.get("descricao")
        preco = request.GET.get("preco")
        empresa_id = request.GET.get("empresa_id")
        restaurante_nome = request.GET.get("restaurante")
        subcategoria_id = request.GET.get("subcategoria_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (descricao):
            query = query.filter(descricao__icontains=descricao)
        if (empresa_id):
            query = query.filter(empresa__id=empresa_id)
        if (restaurante_nome):
            query = query.filter(empresa__nome__icontains=restaurante_nome)
        if (subcategoria_id):
            if not (subcategoria_id == '?'):
                query = query.filter(subcategorias__id=subcategoria_id)


        rows = []

        listasubcategorias = []

        for produto in query:
            for subcategoria in produto.subcategorias.all():
                if not subcategoria in listasubcategorias:
                    listasubcategorias.append(subcategoria)


        for subcategoria_atual in listasubcategorias:
            produtos = []

            for produto in query:
                for subcategoria in produto.subcategorias.all():
                    if subcategoria_atual.id == subcategoria.id:
                        prod = {
                            "id": produto.id,
                            "nome": produto.nome,
                            "descricao": produto.descricao,
                            "preco": produto.preco,
                            "foto": produto.foto,
                            "empresa_id":produto.empresa.id,
                            "empresa":produto.empresa.nome
                        }

                        produtos.append(prod)

            r_sub = {
                "subcategoria": subcategoria_atual.nome,
                "subcategoria_id": subcategoria_atual.id,
                "categoria": subcategoria_atual.categoria.nome,
                "categoria_id": subcategoria_atual.categoria.id,
                "produtos":produtos
            }

            rows.append(r_sub)


        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def produtos(request):
        # Query Base
        query = Produto.objects.all().order_by("nome")

        # Filtros
        nome = request.GET.get("nome")
        id = request.GET.get("id")
        descricao = request.GET.get("descricao")
        preco = request.GET.get("preco")
        empresa_id = request.GET.get("empresa_id")
        restaurante_nome = request.GET.get("restaurante")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (nome):
            query = query.filter(nome__icontains=nome)
        if (id > 0):
            query = query.filter(id=id)
        if (descricao):
            query = query.filter(descricao__icontains=descricao)
        if (empresa_id):
            query = query.filter(empresa__id=empresa_id)
        if (restaurante_nome):
            query = query.filter(empresa__nome__icontains=restaurante_nome)


        rows = []

        for produto in query:

            subs = []
            ops = []
            # fotos = []

            for subcategoria in produto.subcategorias.all():
                r_sub = {
                    "subcategoria":subcategoria.nome,
                    "subcategoria_id":subcategoria.id,
                    "categoria":subcategoria.categoria.nome,
                    "categoria_id":subcategoria.categoria.id
                }
                subs.append(r_sub)

            for opc in produto.opcionais.all().order_by("titulo"):
                opcoes = []

                for opo in opc.Opcoes.all():
                    r_opcao = {
                        "opcao_titulo":opo.titulo,
                        "opcao_valor":opo.valor,
                        "opcao_id":opo.id,
                        "opcao_selecionado":False,
                        "opcao_quantidade":0
                    }

                    opcoes.append(r_opcao)

                r_opc = {
                    "opcional_titulo":opc.titulo,
                    "opcional_tipo":opc.tipo,
                    "opcional_id":opc.id,
                    "opcional_opcoes":opcoes,
                    "opcional_quantidade":opc.quantidade,
                    "opcional_quantidade_selecionado":0
                }

                ops.append(r_opc)

            # for foto in produto.fotos.all():
            #     r_foto = {
            #         "foto_id": foto.id,
            #         "foto_caminho":foto.caminho
            #     }
            #     fotos.append(r_foto)

            r = {
                "id": produto.id,
                "nome": produto.nome,
                "descricao": produto.descricao,
                "preco": produto.preco,
                "foto": produto.foto,
                "empresa_id":produto.empresa.id,
                "empresa":produto.empresa.nome,
                "subcategorias":subs,
                "opcionais":ops
            }

            rows.append(r)


        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')


    # @staticmethod
    # def fotos(request):
    #     # Query Base
    #     query = Foto.objects.all()
    #
    #     # Filtros
    #     id = request.GET.get("id")
    #     produto_id = request.GET.get("produto_id")
    #
    #     if (id == 'undefined'):
    #         id = int()
    #         id = 0
    #
    #     if not (id):
    #         id = int()
    #         id = 0
    #
    #     if (id > 0):
    #         query = query.filter(id=id)
    #     if (produto_id):
    #         query = query.filter(produto__id=produto_id)
    #
    #     lista = serialize('json', query,
    #                       fields=["id", "caminho", "produto__id", "produto__nome"])
    #     return HttpResponse(lista, content_type='application/json')

    # @staticmethod
    # @csrf_exempt
    # def savefoto(request):
    #     # Filtros
    #     id = request.POST.get("id")
    #     caminho = request.POST.get("caminho")
    #     produto_id = request.POST.get("produto_id")
    #
    #     # Objeto de Foto
    #     oFoto = Foto()
    #
    #     if (id):
    #         if (int(id) > 0):
    #             oFoto = Foto.objects.get(id=id)
    #
    #     oFoto.caminho = caminho
    #     oFoto.produto = Produto.objects.filter(id=produto_id)
    #
    #     oFoto.save()
    #
    #     lista = "true"
    #
    #     return HttpResponse(lista, content_type='application/json')

    # @staticmethod
    # def excluirfoto(request):
    #     id = request.GET.get("id")
    #
    #     # Query Base
    #     oFoto = Foto.objects.filter(id=id).first()
    #     oFoto.delete()
    #
    #     lista = "true"
    #     return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def pedidos(request):
        # Query Base
        query = Pedido.objects.all().order_by("-id")

        # Filtros
        id = request.GET.get("id")
        data_inicio = request.GET.get("data_inicio")
        data_fim = request.GET.get("data_fim")
        valor_minimo = request.GET.get("valor_min")
        valor_maximo = request.GET.get("valor_max")
        status = request.GET.get("status")

        cliente_id = request.GET.get("cliente_id")
        empresa_id = request.GET.get("empresa_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (data_inicio):
            if (data_fim):
                query = query.filter(data__gte=data_inicio, data_lte=data_fim)
            else:
                query = query.filter(data=data_inicio)


        if (id > 0):
            query = query.filter(id=id)

        if (cliente_id):
            query = query.filter(cliente__id=cliente_id)

        if(empresa_id):
            query = query.filter(empresa__id=empresa_id)

        if(valor_minimo):
            query = query.filter(total__gte=valor_minimo)

        if(valor_maximo):
            query = query.filter(total__lte=valor_maximo)

        if(status):
            query = query.filter(status=status)

        pedidos_rows = []

        for pedido in query:
            itens_rows = []

            valor_total = 0

            for item in pedido.Itens.all():
                r_item = {
                    "item_id":item.id,
                    "quantidade":item.quantidade,
                    "produto_id":item.produto.id,
                    "produto":item.produto.nome,
                    "observacao":item.observacao,
                    "preco_parcial":(item.quantidade*item.produto.preco),

                }
                itens_rows.append(r_item)

                valor_total = valor_total + (item.quantidade * item.produto.preco)

            oPagamento = pedido.Pagamento.first()
            pagamento_obs = ''
            pagamento_tipo = ''



            if oPagamento:
                pagamento_obs = oPagamento.obs
                pagamento_tipo = oPagamento.tipopagamento

                if oPagamento.cpfnanota:
                    pagamento_obs = pagamento_obs + " -  CPF NA NOTA: SIM - CPF: " + oPagamento.cpf


            r = {
                "id":pedido.id,
                "data":pedido.data.strftime("%Y-%m-%d %H:%m"),
                "total":pedido.total,
                "cliente":pedido.cliente.nome,
                "cliente_id":pedido.cliente.id,
                "empresa":pedido.empresa.nome,
                "empresa_id":pedido.empresa.id,
                "status":pedido.status,
                "endereco":pedido.endereco_entrega + ", " + str(pedido.cliente.numero),
                "bairro":pedido.bairro_entrega.nome,
                "bairro_id":pedido.bairro_entrega.id,
                "cidade":pedido.cidade_entrega.nome,
                "cidade_id":pedido.cidade_entrega.id,
                "componente":pedido.complemento_entrega,
                "pagamento_obs":pagamento_obs,
                "pagamento_tipo":pagamento_tipo,
                "telefone":pedido.empresa.telefone,
                "frete":pedido.total -  valor_total,
                "itens":itens_rows,
                "empresa_logotipo":pedido.empresa.logotipo
            }

            pedidos_rows.append(r)

        lista = json.dumps(list(pedidos_rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savepedido(request):
        # Filtros
        id = request.POST.get("id")
        data = request.POST.get("data")
        cliente_id = request.POST.get("cliente_id")
        endereco = request.POST.get('endereco')
        cidade_id = request.POST.get('cidade_id')
        bairro_id = request.POST.get('bairro_id')
        complemento = request.POST.get('complemento')

        total = 0.0

        listacompras = Carrinho.objects.filter(cliente__id=cliente_id)

        # Objeto de Pedidos
        oPedido = Pedido()

        if (id == 'undefined'):
            id = int()
            id = 0


        if (id):
            if (int(id) > 0):
                oPedido = Pedido.objects.get(id=id)

        oPedido.cliente = Cliente.objects.filter(id=cliente_id).first()

        if data:
            oPedido.data = data


        if(listacompras):
            oPedido.empresa = listacompras[0].produto.empresa


        oPedido.total = 0

        oPedido.endereco_entrega = oPedido.cliente.endereco
        if not endereco == '?':
            if endereco:
                oPedido.endereco_entrega = endereco

        oPedido.cidade_entrega = oPedido.cliente.cidade
        if not cidade_id == '?':
            if cidade_id:
                oPedido.cidade_entrega = Cidade.objects.filter(id=cidade_id).first()

        oPedido.bairro_entrega = oPedido.cliente.bairro
        if not bairro_id == '?':
            if bairro_id:
                oPedido.bairro_entrega = Bairro.objects.filter(id=bairro_id).first()

        if complemento:
            oPedido.complemento_entrega = complemento

        oPedido.status = 'Aguardando o Tipo de Pagamento'

        oPedido.save()

        # Arrumando a lista de itens
        for item_carrinho in listacompras:
            oitem = Item()
            oitem.pedido = oPedido
            oitem.quantidade = item_carrinho.quantidade
            oitem.produto = item_carrinho.produto
            oitem.observacao = item_carrinho.observacao
            total = total + (oitem.quantidade * item_carrinho.preco)

            oitem.save()

        oPedido.total = total
        oPedido.save()

        listacompras.delete()

        return HttpResponse(oPedido.id, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savepedido_status(request):
        # Filtros
        id = request.GET.get("id")
        status = request.GET.get("status")

        oPedido = Pedido.objects.filter(id=id).first()


        oPedido.status = status
        oPedido.save()

        return HttpResponse(oPedido.id, content_type='application/json')


    @staticmethod
    def excluirpedido(request):
        id = request.GET.get("id")

        # Query Base
        oPedido = Pedido.objects.filter(id=id).first()
        oPedido.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def itens(request):
        # Query Base
        query = Pedido.objects.all().order_by("data")

        # Filtros
        id = request.GET.get("id")
        pedido_id = request.GET.get("pedido_id")
        produto_id = request.GET.get("produto_id")
        produto_nome = request.GET.get("produto_nome")
        qtd_minimo = request.GET.get("valor_min")
        qtd_maximo = request.GET.get("valor_max")


        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (id > 0):
            query = query.filter(id=id)

        if (pedido_id):
            query = query.filter(pedido__id=pedido_id)

        if(produto_nome):
            query = query.filter(produto__nome__icontains=produto_nome)

        if(qtd_minimo):
            query = query.filter(quantidade__gte=qtd_minimo)

        if(qtd_maximo):
            query = query.filter(quantidade__lte=qtd_maximo)

        lista = serialize('json', query,fields=["id", "pedido__id", "quantidade", "produto__id", "produto__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveitem(request):
        # Filtros
        id = request.POST.get("id")
        pedido_id= request.POST.get("pedido_id")
        quantidade = request.POST.get("quantidade")
        produto_id = request.POST.get("produto_id")

        # Objeto de Itens
        oItem = Item()

        if (id):
            if (int(id) > 0):
                oItem = Item.objects.get(id=id)


        oItem.quantidade = quantidade
        oItem.pedido = Pedido.objects.filter(id=pedido_id).first()
        oItem.produto = Produto.objects.filter(id=produto_id).first()

        oItem.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluiritem(request):
        id = request.GET.get("id")

        # Query Base
        oItem = Item.objects.filter(id=id).first()
        oItem.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def carrinho(request):
        # Query Base
        cliente_id = request.GET.get("cliente_id")
        ocarrinho = Carrinho.objects.filter(cliente__id=cliente_id)

        rows = []

        sum_compra = 0.0
        frete = 0.0
        tempo_estimado = "Não informado"

        if len(ocarrinho) > 0:
            empresa = ocarrinho[0].produto.empresa
            cliente = ocarrinho[0].cliente
            tempo_estimado = ocarrinho[0].produto.empresa.tempo.nome

            for bairro in empresa.BairrosAtendimento.all():
                if cliente.bairro.id == bairro.bairro.id:
                    frete = bairro.frete

        for item in ocarrinho:
            sum_compra = sum_compra + (item.preco * item.quantidade)

            r = {
                "id":item.id,
                "quantidade":item.quantidade,
                "observacao":item.observacao,
                "produto_id":item.produto.id,
                "produto":item.produto.nome,
                "produto_preco":item.preco,
                "total_parcial":item.quantidade * item.preco
            }

            rows.append(r)

        result = {
            "lista_compra":rows,
            "frete": frete,
            "tempo_estimado": tempo_estimado,
            "total_compra": sum_compra
        }


        lista = json.dumps(result)




        # lista = serialize('json', query)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savecarrinho(request):
        # Filtros
        produto_id= request.POST.get("produto_id")
        quantidade = request.POST.get("quantidade")
        observacao = request.POST.get("observacao")
        cliente_id = request.POST.get("cliente_id")
        valor = request.POST.get("valor")

        # Objeto de Itens
        oCarrinho = Carrinho()

        oCarrinho.quantidade = quantidade
        oCarrinho.observacao = observacao
        oCarrinho.preco = valor
        oCarrinho.cliente = Cliente.objects.filter(id=cliente_id).first()
        oCarrinho.produto = Produto.objects.filter(id=produto_id).first()


        lista_produtos = Carrinho.objects.filter(cliente__id=cliente_id)
        mesmo_restaurante = True

        for item in lista_produtos:
            if not item.produto.empresa.id == oCarrinho.produto.empresa.id:
                mesmo_restaurante = False

        if mesmo_restaurante:
            oCarrinho.save()
            lista = "true"
        else:
            lista = "false"


        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savetipopagamentopedido(request):
        # Filtros
        pedido_id= request.POST.get("id")
        tipopagamento = request.POST.get("tipopagamento")
        oPedido = Pedido.objects.get(id=pedido_id)


        frete = 0.0

        if len(oPedido.Itens.all()) > 0:
            empresa = oPedido.Itens.all()[0].produto.empresa
            cliente = oPedido.cliente

            for bairro in empresa.BairrosAtendimento.all():
                if cliente.bairro.id == bairro.bairro.id:
                    frete = bairro.frete


        oPedido.total = oPedido.total + frete
        oPedido.save()


        # Objeto de Itens
        oPagamento = Pagamento()
        oPagamento.pedido = oPedido
        oPagamento.tipopagamento = tipopagamento
        oPagamento.total = oPedido.total + frete

        oPagamento.save()

        if(tipopagamento == 'na_entrega'):
            oPedido.status = 'Aguardando Aprovacao'
        else:
            oPedido.status = 'Aguardando Pagamento'

        oPedido.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def saveobspagamentopedido(request):
        # Filtros
        pedido_id= request.POST.get("id")
        troco = request.POST.get("troco")
        outro = request.POST.get("outro")
        cpfnanota = request.POST.get("cpfnanota")
        cpf = request.POST.get("cpf")
        bandeira = request.POST.get("bandeira")
        tipo = request.POST.get("tipo")

        oPedido = Pedido.objects.get(id=pedido_id)
        oPedido.status = "Aguardando Aprovacao"

        # Objeto de Itens
        oPagamento = oPedido.Pagamento.get()

        if not troco:
            troco=0

        if cpfnanota == "1":
            oPagamento.cpfnanota = True
            oPagamento.cpf = cpf

        if tipo=="cartao":
            oPagamento.obs = "Cartao - " + bandeira + " - " + outro
        elif tipo=="dinheiro":
            oPagamento.trocopara = troco

        oPagamento.save()
        oPedido.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def efetuarpagamento(request):

        # Pegando o modulo do mercado pago
        mp = mercadopago.MP("APP_USR-4537199727650400-032722-d1fc4d6607a88b1056fb37b48cce299e__LA_LB__-249921863")

        # Corrigindo as variaveis de POST
        token = request.POST.get("token")
        payment_method_id = request.POST.get("paymentMethodId")
        pedido_id = request.POST.get("pedido_id")
        cpfnanota = request.POST.get("cpfnanota")
        cpf = request.POST.get("cpf")

        oPedido = Pedido.objects.filter(id=pedido_id).first()
        oCliente = oPedido.cliente

        frete = 0.0

        if len(oPedido.Itens.all()) > 0:
            empresa = oPedido.Itens.all()[0].produto.empresa
            cliente = oPedido.cliente

            for bairro in empresa.BairrosAtendimento.all():
                if cliente.bairro.id == bairro.bairro.id:
                    frete = bairro.frete


        oPedido.total = oPedido.total + frete
        oPedido.save()

        # Pegando o resultado do MP
        oMp = demjson.decode(request.POST.get("resultado"))

        # Preparando o envio do pagamento
        payment = mp.post("/v1/payments", {
            "transaction_amount": oPedido.total,
            "description": "PG - #" + str(oPedido.id) + " - " + payment_method_id,
            "installments": 1,
            "payment_method_id":payment_method_id,
            "token":token,
            "payer": {
                "email":oCliente.email
            }
        });

        oMPagoResultado = demjson.decode(json.dumps(payment, indent=4))
        oPagamento = oPedido.Pagamento.all().first()

        oPagamento.obs = oMp["id"]
        oPagamento.total = oPedido.total

        if((oMPagoResultado["response"])["status"] == "approved"):
            oPedido.status = "Aguardando Preparo"
        else:
            oPedido.status = "Pagamento Rejeitado"


        if cpfnanota == "1":
            oPagamento.cpfnanota = True
            oPagamento.cpf = cpf


        oPagamento.save()
        oPedido.save()

        return HttpResponse(oPedido.status, content_type='application/json')


    @staticmethod
    def excluircarrinho(request):
        id = request.GET.get("id")

        # Query Base
        oCarrinho = Carrinho.objects.filter(id=id).first()
        oCarrinho.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def getRestaurantes(request):
        id = request.GET.get("id")
        texto = request.GET.get("texto")
        tipocozinha_id = request.GET.get("tipocozinha_id")

        # Query Base
        oCliente = Cliente.objects.filter(id=id).first()

        oRestaurantes = Empresa.objects.filter(BairrosAtendimento__bairro__id=oCliente.bairro.id).order_by("BairrosAtendimento__frete")
        oRestaurantes = oRestaurantes.order_by("-nota")

        if(texto):
            oRestaurantes = oRestaurantes.filter(descricao__icontains=texto)

        if(tipocozinha_id):
            tipocozinha_id = int(tipocozinha_id)
            if(tipocozinha_id>0):
                oRestaurantes = oRestaurantes.filter(tipocozinha__id=tipocozinha_id)

        rows = []

        restaurantes_filtrados = []

        for rest in oRestaurantes:
            if rest.aberturas.filter(fechamento__isnull=True).exists():
                restaurantes_filtrados.append(rest)

        for r in restaurantes_filtrados:

            row = {
                "id":r.id,
                "nome":r.nome,
                "descricao":r.descricao,
                "email":r.email,
                "cidade_id":r.cidade.id,
                "cidade":r.cidade.nome,
                "endereco":r.endereco,
                "bairro_id":r.bairro.id,
                "bairro":r.bairro.nome,
                "telefone":r.telefone,
                "tipocozinha_id":r.tipocozinha.id,
                "tipocozinha":r.tipocozinha.nome,
                "nota":str(r.nota),
                "custo":r.custo,
                "nota_atual":r.nota_atual,
                "aceita_cartao":r.aceita_cartao,
                "aceita_valerefeicao":r.aceita_valerefeicao,
                "aceita_pagamentoonline":r.aceita_pagamentoonline,
                "logotipo":r.logotipo
            }

            rows.append(row)

        # lista = serialize('json',rows)
        lista = json.dumps(list(rows))

        # lista = "true"
        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def getRestaurantesBairro(request):
        bairro = request.GET.get("bairro")
        obairro = Bairro.objects.filter(nome=bairro).first()

        # Query Base
        oRestaurantes = Empresa.objects.filter(BairrosAtendimento__bairro__id=obairro.id).order_by("BairrosAtendimento__frete")
        oRestaurantes = oRestaurantes.order_by("-nota")

        rows = []

        restaurantes_filtrados = []

        for rest in oRestaurantes:
            if rest.aberturas.filter(fechamento__isnull=True).exists():
                restaurantes_filtrados.append(rest)

        for r in restaurantes_filtrados:

            row = {
                "id":r.id,
                "nome":r.nome,
                "descricao":r.descricao,
                "email":r.email,
                "cidade_id":r.cidade.id,
                "cidade":r.cidade.nome,
                "endereco":r.endereco,
                "bairro_id":r.bairro.id,
                "bairro":r.bairro.nome,
                "telefone":r.telefone,
                "tipocozinha_id":r.tipocozinha.id,
                "tipocozinha":r.tipocozinha.nome,
                "nota":str(r.nota),
                "custo":r.custo,
                "nota_atual":r.nota_atual,
                "aceita_cartao":r.aceita_cartao,
                "aceita_valerefeicao":r.aceita_valerefeicao,
                "aceita_pagamentoonline":r.aceita_pagamentoonline,
                "logotipo":r.logotipo
            }

            rows.append(row)

        # lista = serialize('json',rows)
        lista = json.dumps(list(rows))

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def getrestaurantebypedido(request):
        pedido_id = request.GET.get("pedido_id")

        oPedido = Pedido.objects.filter(id=pedido_id).first()

        row = {
            "id":oPedido.empresa.id,
            "nome":oPedido.empresa.nome,
            "descricao":oPedido.empresa.descricao,
            "email":oPedido.empresa.email,
            "cidade_id":oPedido.empresa.cidade.id,
            "cidade":oPedido.empresa.cidade.nome,
            "endereco":oPedido.empresa.endereco,
            "bairro_id":oPedido.empresa.bairro.id,
            "bairro":oPedido.empresa.bairro.nome,
            "telefone":oPedido.empresa.telefone,
            "tipocozinha_id":oPedido.empresa.tipocozinha.id,
            "tipocozinha":oPedido.empresa.tipocozinha.nome,
            "nota":str(oPedido.empresa.nota),
            "custo":oPedido.empresa.custo,
            "nota_atual":oPedido.empresa.nota_atual,
            "aceita_cartao":oPedido.empresa.aceita_cartao,
            "aceita_valerefeicao":oPedido.empresa.aceita_valerefeicao,
            "aceita_pagamentoonline": oPedido.empresa.aceita_pagamentoonline,
            "restaurante_status":oPedido.empresa.status,
            "logotipo":oPedido.empresa.logotipo
        }

        # lista = serialize('json',rows)
        lista = json.dumps(row)

        # lista = "true"
        return HttpResponse(lista, content_type='application/json')


    # @staticmethod
    # def tipospagamentos(request):
    #     # Query Base
    #
    #     tipo_id = request.GET.get("tipopagamento_id")
    #     titulo = request.GET.get("titulo")
    #
    #     listas_tipospagamentos = TipoPagamento.objects.all()
    #
    #     if tipo_id:
    #         listas_tipospagamentos = listas_tipospagamentos.filter(id=tipo_id)
    #
    #     if titulo:
    #         listas_tipospagamentos = listas_tipospagamentos.filter(titulo__icontains=titulo)
    #
    #
    #     # lista = json.dumps(list(listas_tipospagamentos))
    #
    #     lista = serialize('json', listas_tipospagamentos)
    #     return HttpResponse(lista, content_type='application/json')


    @staticmethod
    def bandeiras(request):
        id = request.GET.get("id")
        titulo = request.GET.get("titulo")
        tipo = request.GET.get("tipo")

        # Query Base
        obandeiras = Bandeira.objects.all()

        if(id):
            obandeiras = obandeiras.filter(id=id)

        if(titulo):
            obandeiras = obandeiras.filter(titulo__icontains=titulo)

        if(tipo):
            obandeiras = obandeiras.filter(tipo__icontains=tipo)

        lista = json.dumps(serialize('json', obandeiras))

        return HttpResponse(lista, content_type='application/json')


    @staticmethod
    @csrf_exempt
    def savemensalidade(request):
        # Filtros
        empresa_id = request.POST.get("empresa_id")
        id = request.POST.get("id")
        status = request.POST.get("status")

        lista_empresas = Empresa.objects.all()

        if (empresa_id):
            if (empresa_id == 'undefined'):
                empresa_id = 0
        if int(empresa_id) > 0:
            lista_empresas = Empresa.objects.filter(empresa__id=empresa_id)


        data_atual = datetime.now()


        for oEmpresa in lista_empresas:
            # Objeto de Mensalidades
            oMensalidade = Mensalidade()


            if (id):
                if (id == 'undefined'):
                    id = 0

            if (int(id) > 0):
                oMensalidade = Mensalidade.objects.get(id=id)
            else:
                oMensalidade.titulo = oEmpresa.nome + "_" + str(data_atual.year) + str(data_atual.month) + str(data_atual.day)
                oMensalidade.valor = oEmpresa.valor_mensalidade
                oMensalidade.empresa = oEmpresa
                oMensalidade.data_cobranca = data_atual

            oMensalidade.status = status

            if not status == "Aguardando Pagamento":
                oMensalidade.data_pagamento = data_atual

            oMensalidade.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirmensalidade(request):
        id = request.GET.get("id")

        # Query Base
        oMensalidade = Mensalidade.objects.filter(id=id).first()
        oMensalidade.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def mensalidades(request):
        # Query Base
        query = Mensalidade.objects.all().order_by("-data_cobranca")

        # Filtros
        data = request.GET.get("data")
        status = request.GET.get("status")
        empresa_id = request.GET.get("empresa_id")
        id = request.GET.get("id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (status):
            query = query.filter(status__icontains=status)
        if (id > 0):
            query = query.filter(id=id)
        if (data):
            query = query.filter(data_cobranca__gte=data, data_cobranca__lte=data)
        if (empresa_id):
            query = query.filter(empresa__id=empresa_id)


        rows = []

        for mensalidade in query:

            data_pagamento =''

            if mensalidade.data_pagamento:
                data_pagamento = mensalidade.data_pagamento.strftime('%d-%m-%Y')

            r = {
                "id": mensalidade.id,
                "valor": mensalidade.valor,
                "titulo": mensalidade.titulo,
                "empresa_nome": mensalidade.empresa.nome,
                "empresa_id": mensalidade.empresa.id,
                "data_pagamento":data_pagamento,
                "data_cobranca":mensalidade.data_cobranca.strftime('%d-%m-%Y'),
                "status":mensalidade.status
            }

            rows.append(r)


        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')