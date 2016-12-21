"""game7api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adm/login/', adminLoginView.as_view(), name = "Login"),
    url(r'^adm/home/', adminHomeView.as_view(), name = "Home-adm"),

    url(r'^adm/categorias/', adminCategoriasView.as_view(), name = "Categorias-adm"),
    url(r'^adm/categorias-nova', adminCategoriaNovaView.as_view(), name = "NovaCategoria-adm"),
    url(r'^adm/categoria-excluir$', adminCategoriaExcluirView.as_view(), name = "ExcluirCategoria-adm"),
    url(r'^adm/categoria-ver', adminCategoriaVerView.as_view(), name="VerCategoria-adm"),
    url(r'^adm/categoria-edicao', adminCategoriaEdicaoView.as_view(), name="EdicaoCategoria-adm"),
    url(r'^adm/bd-categoria-excluir$', dbadmincategoriaexcluir, name = "BDExcluirCategoria-adm"),

    url(r'^adm/subcategorias/', adminSubCategoriasView.as_view(), name="SubCategorias-adm"),
    url(r'^adm/subcategorias-nova', adminSubCategoriaNovaView.as_view(), name="NovaSubCategoria-adm"),
    url(r'^adm/subcategoria-excluir$', adminSubCategoriaExcluirView.as_view(), name="ExcluirSubCategoria-adm"),
    url(r'^adm/subcategoria-ver', adminSubCategoriaVerView.as_view(), name="VerSubCategoria-adm"),
    url(r'^adm/subcategoria-edicao', adminSubCategoriaEdicaoView.as_view(), name="EdicaoSubCategoria-adm"),
    url(r'^adm/bd-subcategoria-excluir$', dbadminsubcategoriaexcluir, name = "BDExcluirSubCategoria-adm"),

    url(r'^adm/clientes/', adminClientesView.as_view(), name="Clientes-adm"),
    url(r'^adm/clientes-nova/', adminClientesNovaView.as_view(), name="NovoCliente-adm"),
    url(r'^$', adminHomeView.as_view(), name = "Home"),
]
