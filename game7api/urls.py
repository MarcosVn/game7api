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
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', adminHomeView.as_view(), name="Home"),
    url(r'^admin/', admin.site.urls),
    url(r'^adm/login/', adminLoginView.as_view(), name = "Login"),
    url(r'^adm/$', adminHomeView.as_view(), name = "Home-adm"),
    url(r'^adm/categorias/', adminCategoriasView.as_view(), name = "Categorias-adm"),
    url(r'^adm/categorias-nova', adminCategoriaNovaView.as_view(), name = "NovaCategoria-adm"),
    url(r'^adm/categoria-excluir$', adminCategoriaExcluirView.as_view(), name = "ExcluirCategoria-adm"),
    url(r'^adm/categoria-ver', adminCategoriaVerView.as_view(), name="VerCategoria-adm"),
    url(r'^adm/categoria-edicao', adminCategoriaEdicaoView.as_view(), name="EdicaoCategoria-adm"),
    url(r'^adm/subcategorias/', adminSubCategoriasView.as_view(), name="SubCategorias-adm"),
    url(r'^adm/subcategorias-nova', adminSubCategoriaNovaView.as_view(), name="NovaSubCategoria-adm"),
    url(r'^adm/subcategoria-excluir$', adminSubCategoriaExcluirView.as_view(), name="ExcluirSubCategoria-adm"),
    url(r'^adm/subcategoria-ver', adminSubCategoriaVerView.as_view(), name="VerSubCategoria-adm"),
    url(r'^adm/subcategoria-edicao', adminSubCategoriaEdicaoView.as_view(), name="EdicaoSubCategoria-adm"),
    url(r'^adm/produtos/', adminProdutosView.as_view(), name="Produtos-adm"),
    url(r'^adm/produto-nova', adminProdutoNovaView.as_view(), name="NovaProduto-adm"),
    url(r'^adm/produto-excluir$', adminProdutoExcluirView.as_view(), name="ExcluirProduto-adm"),
    url(r'^adm/produto-ver', adminProdutoVerView.as_view(), name="VerProduto-adm"),
    url(r'^adm/produto-edicao', adminProdutoEdicaoView.as_view(), name="EdicaoProduto-adm"),
    url(r'^adm/produto-galeria', adminProdutoGaleriaView.as_view(), name="GaleriaProduto-adm"),
    url(r'^adm/produto-categorias$', adminProdutoCategoriasView.as_view(), name="CategoriasProduto-adm"),
    url(r'^adm/produto-categorias-excluir', adminProdutoCategoriasExcluirView.as_view(), name="CategoriasProduto-adm"),
    url(r'^adm/produto-categorias-novo', adminProdutoCategoriasNovoView.as_view(), name="CategoriasProduto-adm"),
    url(r'^adm/clientes/', adminClientesView.as_view(), name="Clientes-adm"),
    url(r'^adm/clientes-nova/', adminClienteNovaView.as_view(), name="NovoCliente-adm"),
    url(r'^adm/cliente-excluir/', adminClienteExcluirView.as_view(), name="ExcluirCliente-adm"),
    url(r'^adm/cliente-ver/', adminClienteVerView.as_view(), name="VerCliente-adm"),
    url(r'^adm/cliente-edicao/', adminClienteEdicaoView.as_view(), name="EdicaoCliente-adm"),
    url(r'^adm/filiados/', adminEmpresasView.as_view(), name="Empresas-adm"),
    url(r'^adm/filiado-nova/', adminEmpresaNovaView.as_view(), name="NovoEmpresa-adm"),
    url(r'^adm/filiado-excluir/', adminEmpresaExcluirView.as_view(), name="ExcluirEmpresa-adm"),
    url(r'^adm/filiado-ver/', adminEmpresaVerView.as_view(), name="VerEmpresa-adm"),
    url(r'^adm/filiado-edicao/', adminEmpresaEdicaoView.as_view(), name="EdicaoEmpresa-adm"),
    url(r'^adm/filiado/atendimentos/', adminAtendimentosView.as_view(), name="AtendimentosEmpresa-adm"),
    url(r'^adm/filiado/atendimento-novo', adminAtendimentoNovaView.as_view(), name="NovoAtendimentosEmpresa-adm"),
    url(r'^adm/filiado/atendimento-excluir', adminAtendimentoExcluirView.as_view(), name="ExcluirAtendimentosEmpresa-adm"),
    url(r'^adm/funcionarios/', adminFuncionariosView.as_view(), name="Categorias-adm"),
    url(r'^adm/funcionario-nova', adminFuncionarioNovaView.as_view(), name="NovaCategoria-adm"),
    url(r'^adm/funcionario-excluir$', adminFuncionarioExcluirView.as_view(), name="ExcluirCategoria-adm"),
    url(r'^adm/funcionario-ver', adminFuncionarioVerView.as_view(), name="VerCategoria-adm"),
    url(r'^adm/funcionario-edicao', adminFuncionarioEdicaoView.as_view(), name="EdicaoCategoria-adm"),
    url(r'^adm/pedidos/', adminPedidosView.as_view(), name="Pedidos-adm"),
    url(r'^adm/pedido-nova', adminPedidoNovaView.as_view(), name="NovaPedido-adm"),
    url(r'^adm/pedido-excluir$', adminPedidoExcluirView.as_view(), name="ExcluirPedido-adm"),
    url(r'^adm/pedido-ver', adminPedidoVerView.as_view(), name="VerPedido-adm"),

    url(r'^adm/tiposcozinha/', adminTiposCozinhaView.as_view(), name="TiposCozinhas-adm"),
    url(r'^adm/tipocozinha-nova', adminTipoCozinhaNovaView.as_view(), name="NovaTipoCozinha-adm"),
    url(r'^adm/tipocozinha-excluir$', adminTipoCozinhaExcluirView.as_view(), name="ExcluirTipoCozinha-adm"),
    url(r'^adm/tipocozinha-ver', adminTipoCozinhaVerView.as_view(), name="VerTipoCozinha-adm"),
    url(r'^adm/tipocozinha-edicao', adminTipoCozinhaEdicaoView.as_view(), name="EdicaoTipoCozinha-adm"),


    url(r'^js/categorias', ServiceJson.categorias, name='categorias'),
    url(r'^js/clientes', ServiceJson.clientes, name='clientes'),
    url(r'^js/cliente-login', ServiceJson.clienteLogin, name='clientelogin'),
    url(r'^js/subcategorias', ServiceJson.subcategorias, name='subcategorias'),
    url(r'^js/estados', ServiceJson.estados, name='estados'),
    url(r'^js/cidades', ServiceJson.cidades, name='Cidades'),
    url(r'^js/bairros', ServiceJson.bairros, name='bairros'),
    url(r'^js/empresas', ServiceJson.empresas, name='empresas'),
    url(r'^js/empresa-login', ServiceJson.empresaLogin, name='empresaLogin'),
    url(r'^js/funcionarios', ServiceJson.funcionarios, name='funcionarios'),
    url(r'^js/funcionario-login', ServiceJson.funcionarioLogin, name='funcionariologin'),
    url(r'^js/Repasses', ServiceJson.Repasses, name='Repasses'),
    url(r'^js/produtos', ServiceJson.produtos, name='produtos'),
    url(r'^js/fotos', ServiceJson.fotos, name='fotos'),
    url(r'^js/pedidos', ServiceJson.pedidos, name='pedidos'),
    url(r'^js/tiposcozinhas', ServiceJson.tiposcozinhas, name='tiposcozinhas'),
    url(r'^js/itens', ServiceJson.itens, name='itens'),
    url(r'^js/carrinho', ServiceJson.carrinho, name='carrinho'),
    # url(r'^js/tipospagamentos', ServiceJson.tipospagamentos, name='tipospagamentos'),

    url(r'^js/savecategoria', ServiceJson.savecategoria, name='savecategoria'),
    url(r'^js/savecliente', ServiceJson.savecliente, name='savecliente'),
    url(r'^js/savesubcategoria', ServiceJson.savesubcategoria, name='savesubcategoria'),
    url(r'^js/saveprodutosubcategoria$', ServiceJson.saveprodutosubcategoria, name='saveprodutosubcategoria'),
    url(r'^js/saveprodutofoto$', ServiceJson.saveprodutofoto, name='saveprodutofoto'),
    url(r'^js/saveestado', ServiceJson.saveestado, name='saveestado'),
    url(r'^js/savecidade', ServiceJson.savecidade, name='savecidade'),
    url(r'^js/savebairro', ServiceJson.savebairro, name='savebairro'),
    url(r'^js/saveempresa$', ServiceJson.saveempresa, name='saveempresa'),
    url(r'^js/saveempresabairro$', ServiceJson.saveempresabairro, name='saveempresabairro'),
    url(r'^js/savefuncionario', ServiceJson.savefuncionario, name='savefuncionario'),
    url(r'^js/saverepasse', ServiceJson.saverepasse, name='saverepasse'),
    url(r'^js/saveproduto', ServiceJson.saveproduto, name='saverproduto'),
    url(r'^js/savefoto', ServiceJson.savefoto, name='savefoto'),
    url(r'^js/savepedido', ServiceJson.savepedido, name='savepedido'),
    url(r'^js/saveitem', ServiceJson.saveitem, name='saveitem'),
    url(r'^js/savetipocozinha', ServiceJson.savetipocozinha, name='savetipocozinha'),
    url(r'^js/savecarrinho', ServiceJson.savecarrinho, name='savecarrinho'),
    url(r'^js/savetipopagamentopedido', ServiceJson.savetipopagamentopedido, name='savetipopagamentopedido'),
    url(r'^js/saveobspagamentopedido', ServiceJson.saveobspagamentopedido, name='saveobspagamentopedido'),


    url(r'^js/excluircategoria', ServiceJson.excluircategoria, name='excluircategoria'),
    url(r'^js/excluircliente', ServiceJson.excluircliente, name='excluircliente'),
    url(r'^js/excluirsubcategoria', ServiceJson.excluirsubcategoria, name='excluirsubcategoria'),
    url(r'^js/excluirempresa$', ServiceJson.excluirempresa, name='excluirempresa'),
    url(r'^js/excluirempresa_bairro$', ServiceJson.excluirempresa_bairro, name='excluirempresa_bairro'),
    url(r'^js/excluirprodutosubcategoria$', ServiceJson.excluirproduto_categoria, name='excluirproduto_categoria'),
    url(r'^js/excluirproduto_foto$', ServiceJson.excluirproduto_foto, name='excluirproduto_foto'),
    url(r'^js/excluirfuncionario', ServiceJson.excluirfuncionario, name='excluirfuncionario'),
    url(r'^js/excluirrepasse', ServiceJson.excluirrepasse, name='excluirrepasse'),
    url(r'^js/excluirproduto$', ServiceJson.excluirproduto, name='excluirproduto'),
    url(r'^js/excluirfoto', ServiceJson.excluirfoto, name='excluirfoto'),
    url(r'^js/excluirpedido', ServiceJson.excluirpedido, name='excluirpedido'),
    url(r'^js/excluirtipocozinha', ServiceJson.excluirtipocozinha, name='excluirtipocozinha'),
    url(r'^js/excluircarrinho', ServiceJson.excluircarrinho, name='excluircarrinho'),

    url(r'^js/abrirempresa', ServiceJson.abrirempresa, name='abrirempresa'),
    url(r'^js/fecharempresa', ServiceJson.fecharempresa, name='fecharempresa'),
    url(r'^js/getabertura', ServiceJson.getabertura, name='getabertura'),
    url(r'^js/getrestaurantes', ServiceJson.getRestaurantes, name='getRestaurantes'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)