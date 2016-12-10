from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from core.models import *
from django.template.context import RequestContext


class adminLoginView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render_to_response('adm/login.html', context, RequestContext(request))


class adminHomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render_to_response('adm/home.html', context, RequestContext(request))


class adminCategoriasView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        context['listacategorias'] = Categoria.objects.all()

        return render_to_response('adm/categoria/categorias.html', context, RequestContext(request))


class adminCategoriaNovaView(View):
    def get(self,request, *args, **kwargs):
        context = {}

        return render(request, 'adm/categoria/novo.html', context)

    def post(self,request, *args, **kwargs):

        oCategoria = Categoria()
        oCategoria.nome = request.POST.get("nome")

        oCategoria.save()

        return redirect('/adm/categorias/')


class adminCategoriaEdicaoView(View):
    def get(self,request, *args, **kwargs):
        context = {}

        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()
        context["categoriaselecionado"] = oCategoria

        print oCategoria
        return render(request, 'adm/categoria/editar.html', context)

    def post(self,request, *args, **kwargs):

        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()
        oCategoria.nome = request.POST.get("nome")



        oCategoria.save()

        return redirect('/adm/categorias/')


class adminCategoriaExcluirView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()
        context["categoriaselecionado"]=oCategoria

        return render_to_response('adm/categoria/excluir.html', context, RequestContext(request))


class adminCategoriaVerView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()
        context["categoriaselecionado"]=oCategoria

        return render_to_response('adm/categoria/ver.html', context, RequestContext(request))


class adminSubCategoriasView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()
        context['categoriaselecionado'] = oCategoria

        return render_to_response('adm/subcategoria/subcategorias.html', context, RequestContext(request))


def dbadmincategoriaexcluir(request):

    oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()

    oCategoria.delete()

    return redirect('/adm/categorias/')