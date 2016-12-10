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


class adminSubCategoriaNovaView(View):
    def get(self,request, *args, **kwargs):
        context = {}
        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()

        context["categoriaselecionada"] = oCategoria

        return render(request, 'adm/subcategoria/novo.html', context)

    def post(self,request, *args, **kwargs):
        oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()

        oCategoriaSub = SubCategoria()
        oCategoriaSub.nome = request.POST.get("nome")
        oCategoriaSub.categoria = oCategoria

        oCategoriaSub.save()

        return redirect('/adm/categorias?c_id='+str(oCategoria.id))


class adminSubCategoriaExcluirView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        oSubCategoria = SubCategoria.objects.filter(id=request.GET.get("subc_id")).first()
        context["subcategoriaselecionado"]=oSubCategoria

        return render_to_response('adm/subcategoria/excluir.html', context, RequestContext(request))


def dbadmincategoriaexcluir(request):

    oCategoria = Categoria.objects.filter(id=request.GET.get("c_id")).first()

    id_c = oCategoria.id

    oCategoria.delete()

    return redirect('/adm/categorias?c_id='+str(id_c))


def dbadminsubcategoriaexcluir(request):

    oSubCategoria = SubCategoria.objects.filter(id=request.GET.get("subc_id")).first()

    oSubCategoria.delete()

    return redirect('/adm/categorias')