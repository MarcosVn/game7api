from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from core.models import *
from django.template.context import RequestContext
from django.core.serializers import serialize
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import *
import json
import base64
import random
import re


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
class adminProdutoGaleriaView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/galeria/fotos.html', {}, RequestContext(request))

class adminProdutoCategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/subcategorias.html', {}, RequestContext(request))
class adminProdutoCategoriasExcluirView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/excluir.html', {}, RequestContext(request))
class adminProdutoCategoriasNovoView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('adm/produtocategorias/novo.html', {}, RequestContext(request))

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

class ServiceJson(View):
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
    def excluircategoria(request):
        id = request.GET.get("id")

        # Query Base
        oCategoria = Categoria.objects.filter(id=id).first()

        oCategoria.delete()

        lista = "true"

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
            r = {
                "id":cliente.id,
                "nome":cliente.nome,
                "email":cliente.email,
                "telefone":cliente.telefone,
                "endereco":cliente.endereco,
                "cidade":cliente.cidade.nome,
                "cidade_id":cliente.cidade.id,
                "bairro":cliente.bairro.nome,
                "bairro_id":cliente.bairro.id,
                "estado":cliente.cidade.estado.nome,
                "estado_id":cliente.cidade.estado.id
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
            r = {
                "id":cliente.id,
                "nome":cliente.nome,
                "email":cliente.email,
                "telefone":cliente.telefone,
                "endereco":cliente.endereco,
                "cidade":cliente.cidade.nome,
                "cidade_id":cliente.cidade.id,
                "bairro":cliente.bairro.nome,
                "bairro_id":cliente.bairro.id,
                "estado":cliente.cidade.estado.nome,
                "estado_id":cliente.cidade.estado.id
            }

            rows.append(r)
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


        print "id_"+id
        print "nome_"+nome
        print "email_"+email
        print "senha_"+senha
        print "telefone_"+telefone
        print "endereco_"+endereco
        print "bairro_id_"+bairro_id
        print "cidade_id_"+cidade_id


        # Objeto de Clientes
        oCliente = Cliente()

        if (id):
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

            for bairro in empresa.bairros_atendimento.all():
                r_bairro = {
                    "bairro":bairro.nome,
                    "bairro_id":bairro.id
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
                "descricao":empresa.descricao
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

        if cidade_id:
            oEmpresa.cidade = Cidade.objects.filter(id=cidade_id).first()

        if estado_id:
            oEmpresa.estado = Estado.objects.filter(id=estado_id).first()

        if bairro_id:
            oEmpresa.bairro = Bairro.objects.filter(id=bairro_id).first()

        if endereco:
            oEmpresa.endereco=endereco

        oEmpresa.save()

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
            for bairro in empresa.bairros_atendimento.all():
                r_bairro ={
                    "bairro":bairro.nome,
                    "bairro_id":bairro.id
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
                "bairros_atendimento":rows
            }

        lista = json.dumps(r)
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveempresabairro(request):
        # Filtros
        id = request.POST.get("id")
        bairro_id = request.POST.get("bairro")

        # Objeto de Empresa
        oEmpresa = Empresa.objects.filter(id=id).first()
        oBairro = Bairro.objects.filter(id=bairro_id).first()

        oEmpresa.bairros_atendimento.add(oBairro)
        oEmpresa.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirempresa_bairro(request):
        empresa_id = request.GET.get("empresa_id")
        bairro_id = request.GET.get("bairro_id")

        # Query Base
        oEmpresa = Empresa.objects.filter(id=empresa_id).first()
        oBairro = Bairro.objects.filter(id=bairro_id).first()

        oEmpresa.bairros_atendimento.remove(oBairro)
        oEmpresa.save()

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
    def funcionarios(request):
        # Query Base
        query = Funcionario.objects.all().order_by("nome")

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
    def Repasses(request):
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


        rows = []

        for produto in query:

            subs = []
            fotos = []

            for subcategoria in produto.subcategorias.all():
                r_sub = {
                    "subcategoria":subcategoria.nome,
                    "subcategoria_id":subcategoria.id,
                    "categoria":subcategoria.categoria.nome,
                    "categoria_id":subcategoria.categoria.id
                }
                subs.append(r_sub)

            for foto in produto.fotos.all():
                r_foto = {
                    "foto_id": foto.id,
                    "foto_caminho":foto.caminho
                }
                fotos.append(r_foto)

            r = {
                "id": produto.id,
                "nome": produto.nome,
                "descricao": produto.descricao,
                "preco": produto.preco,
                "foto": produto.foto,
                "empresa_id":produto.empresa.id,
                "empresa":produto.empresa.nome,
                "subcategorias":subs,
                "fotos":fotos
            }

            rows.append(r)


        lista = json.dumps(list(rows))
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveprodutofoto(request):
        # Filtros
        id = request.POST.get("id")
        foto = request.POST.get("foto")
        random_n = random.randint(1, 500000000)

        oProduto = Produto.objects.filter(id=id).first()

        filename = str(oProduto.id) + '_' + str(random_n) + '.jpg'

        image_data = open(settings.BASE_DIR + '/game7api/static/media/produto/' + filename, "wb")
        image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
        image_data.close()

        oFoto = Foto()
        oFoto.caminho = filename
        oFoto.produto = oProduto
        oFoto.save()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def saveprodutosubcategoria(request):
        # Filtros
        id = request.POST.get("id")
        subcategoria_id = request.POST.get("subcategoria_id")

        print id
        print subcategoria_id

        oProduto = Produto.objects.filter(id=id).first()
        oSubcategoria = SubCategoria.objects.filter(id=subcategoria_id).first()

        oProduto.subcategorias.add(oSubcategoria)
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
    def excluirproduto_foto(request):
        foto_id = request.GET.get("f_id")

        # Query Base
        oFoto = Foto.objects.filter(id=foto_id).first()
        oFoto.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

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

        # Objeto de Produtos
        oProduto = Produto()

        if (id):
            if (id == 'undefined'):
                id = 0

            if (int(id) > 0):
                oProduto = Produto.objects.get(id=id)

        oProduto.nome=nome
        oProduto.descricao=descricao
        oProduto.preco=preco
        oProduto.empresa = Empresa.objects.filter(id=empresa_id).first()
        oProduto.save()

        filename = str(oProduto.id) + '_' + str(random_n) + '.jpg'
        image_data = open(settings.BASE_DIR + '/game7api/static/media/produto/' + filename, "wb")
        image_data.write(re.sub('^data:image/.+;base64,', '', foto).decode('base64'))
        image_data.close()

        oProduto.foto = filename
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
    def fotos(request):
        # Query Base
        query = Foto.objects.all()

        # Filtros
        id = request.GET.get("id")
        produto_id = request.GET.get("produto_id")

        if (id == 'undefined'):
            id = int()
            id = 0

        if not (id):
            id = int()
            id = 0

        if (id > 0):
            query = query.filter(id=id)
        if (produto_id):
            query = query.filter(produto__id=produto_id)

        lista = serialize('json', query,
                          fields=["id", "caminho", "produto__id", "produto__nome"])
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    @csrf_exempt
    def savefoto(request):
        # Filtros
        id = request.POST.get("id")
        caminho = request.POST.get("caminho")
        produto_id = request.POST.get("produto_id")

        # Objeto de Foto
        oFoto = Foto()

        if (id):
            if (int(id) > 0):
                oFoto = Foto.objects.get(id=id)

        oFoto.caminho = caminho
        oFoto.produto = Produto.objects.filter(id=produto_id)

        oFoto.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def excluirfoto(request):
        id = request.GET.get("id")

        # Query Base
        oFoto = Foto.objects.filter(id=id).first()
        oFoto.delete()

        lista = "true"
        return HttpResponse(lista, content_type='application/json')

    @staticmethod
    def pedidos(request):
        # Query Base
        query = Pedido.objects.all().order_by("data")

        # Filtros
        id = request.GET.get("id")
        data_inicio = request.GET.get("data_inicio")
        data_fim = request.GET.get("data_fim")
        valor_minimo = request.GET.get("valor_min")
        valor_maximo = request.GET.get("valor_max")


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
                query = query.filter(data__gte=data_inicio)


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

        pedidos_rows = []

        for pedido in query:
            itens_rows = []

            for item in pedido.Itens.all():
                r_item = {
                    "item_id":item.id,
                    "quantidade":item.quantidade,
                    "produto_id":item.produto.id,
                    "produto":item.produto.nome
                }
                itens_rows.append(r_item)

            r = {
                "id":pedido.id,
                "data":pedido.data.strftime("%Y-%m-%d"),
                "total":pedido.total,
                "cliente":pedido.cliente.nome,
                "cliente_id":pedido.cliente.id,
                "empresa":pedido.empresa.nome,
                "empresa_id":pedido.empresa.id,
                "itens":itens_rows
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
        total = request.POST.get("total")
        cliente_id = request.POST.get("cliente_id")
        empresa_id = request.POST.get("empresa_id")

        # Objeto de Pedidos
        oPedido = Pedido()

        if (id):
            if (int(id) > 0):
                oPedido = Pedido.objects.get(id=id)


        oPedido.data = data
        oPedido.total = total
        oPedido.cliente = Cliente.objects.filter(id=cliente_id).first()
        oPedido.empresa = Empresa.objects.filter(id=empresa_id).first()

        oPedido.save()

        lista = "true"

        return HttpResponse(lista, content_type='application/json')

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