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
    url(r'^$', HomeView.as_view(), name="Home"),
    url(r'^admin/', adminHomeView.as_view(), name="Home Admin"),
    url(r'^politica-privacidade/', politicaprivacidadeView.as_view(), name = "Politica-privacidade"),
    url(r'^sobre/', sobreView.as_view(), name="sobre"),
    url(r'^busca/', buscarView.as_view(), name="buscar"),
    url(r'^cadastro-login/', cadastrarLogarView.as_view(), name="buscar"),



    url(r'^restaurante/$', restauranteHomeView.as_view(), name = "RestauranteHome"),
    url(r'^restaurante/login$', restauranteLoginView.as_view(), name = "RestauranteLogin"),
    url(r'^restaurante/perfil$', restaurantePerfilView.as_view(), name = "RestaurantePerfil"),
    url(r'^restaurante/expediente$', restauranteExpedienteView.as_view(), name = "RestaurantePerfil"),
    url(r'^restaurante/cardapio$', restauranteCardapioView.as_view(), name = "RestauranteCardapio"),
    url(r'^restaurante/cardapio/novo$', restauranteCardapioNovoView.as_view(), name = "RestauranteCardapioNovo"),
    url(r'^restaurante/cardapio/editar$', restauranteCardapioEditarView.as_view(), name = "RestauranteCardapioEditar"),
    url(r'^restaurante/cardapio/excluir$', restauranteCardapioExcluirView.as_view(), name = "RestauranteCardapioExcluir"),
    url(r'^restaurante/cardapio/categorias$', restauranteCardapioCategoriasView.as_view(), name = "RestauranteCardapioCategorias"),
    url(r'^restaurante/cardapio/categorias/nova$', restauranteCardapioCategoriasNovaView.as_view(), name = "RestauranteCardapioCategoriasNova"),
    url(r'^restaurante/cardapio/categorias/excluir$', restauranteCardapioCategoriasExcluirView.as_view(), name = "RestauranteCardapioCategoriasExcluir"),
    url(r'^restaurante/repasse$', restauranteRepasseView.as_view(), name = "RestauranteRepasse"),
    url(r'^restaurante/pedidos', restaurantePedidosView.as_view(), name = "RestaurantePedidos"),
    url(r'^restaurante/avaliacoes', restauranteAvaliacoesView.as_view(), name = "RestauranteAvaliacoes"),
    url(r'^restaurante/atendimento/novo', restauranteAtendimentoNovoView.as_view(), name = "RestauranteAtendimentoNovo"),
    url(r'^restaurante/atendimento/excluir', restauranteAtendimentoExcluirView.as_view(), name = "RestauranteAtendimentoExcluir"),

    url(r'^cliente/$', clienteHomeView.as_view(), name = "ClienteHome"),
    url(r'^cliente/perfil$', clientePerfilView.as_view(), name = "ClientePerfil"),
    url(r'^cliente/pedidos$', clientePedidosView.as_view(), name = "ClientePedidos"),
    url(r'^cliente/restaurante$', clienteRestauranteView.as_view(), name = "ClienteRestaurante"),
    url(r'^cliente/produto$', clienteProdutoView.as_view(), name = "ClienteProduto"),
    url(r'^cliente/realizarpedido/endereco', clienteRealizarPedidoEnderecoView.as_view(), name = "ClienteRealizarPedidoEndereco"),
    url(r'^cliente/realizarpedido/tipopagamento', clienteRealizarPedidoTipoPagamentoView.as_view(), name = "ClienteRealizarPedidoTipoPagamento"),
    url(r'^cliente/realizarpedido/pagamento-naentrega', clienteRealizarPedidoPagamentoNaEntregaView.as_view(), name = "ClienteRealizarPedidoPagamentoNaEntrega"),
    url(r'^cliente/realizarpedido/pagamento$', clienteRealizarPedidoPagamentoView.as_view(), name = "ClienteRealizarPedidoPagamentoNaEntrega"),
    url(r'^cliente/pedido', clientePedidoIntegraView.as_view(), name = "ClientePedidoIntegra"),
    url(r'^cliente/avaliacao', clienteAvaliacaoView.as_view(), name = "ClienteAvaliacao"),


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
    # url(r'^adm/produto-galeria', adminProdutoGaleriaView.as_view(), name="GaleriaProduto-adm"),

    url(r'^adm/produto-categorias$', adminProdutoCategoriasView.as_view(), name="CategoriasProduto-adm"),
    url(r'^adm/produto-categorias-excluir', adminProdutoCategoriasExcluirView.as_view(), name="CategoriasProduto-adm"),
    url(r'^adm/produto-categorias-novo', adminProdutoCategoriasNovoView.as_view(), name="CategoriasProduto-adm"),

    url(r'^adm/produto-opcionais$', adminProdutoOpcionaisView.as_view(), name="ProdutoOpcionais-adm"),
    url(r'^adm/produto-opcionais-excluir', adminProdutoOpcionaisExcluirView.as_view(), name="ProdutoOpcionaisExcluir-adm"),
    url(r'^adm/produto-opcionais-novo', adminProdutoOpcionaisNovoView.as_view(), name="ProdutoOpcionaisNovo-adm"),

    url(r'^adm/clientes/', adminClientesView.as_view(), name="Clientes-adm"),
    url(r'^adm/clientes-nova/', adminClienteNovaView.as_view(), name="NovoCliente-adm"),
    url(r'^adm/cliente-excluir/', adminClienteExcluirView.as_view(), name="ExcluirCliente-adm"),
    url(r'^adm/cliente-ver/', adminClienteVerView.as_view(), name="VerCliente-adm"),
    url(r'^adm/cliente-edicao/', adminClienteEdicaoView.as_view(), name="EdicaoCliente-adm"),

    url(r'^adm/mensalidades/', adminMensalidadesView.as_view(), name="Mensalidades-adm"),
    url(r'^adm/cliente-recuperarsenha/', adminClienteRecuperarSenha.as_view(), name="EdicaoCliente-adm"),

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

    url(r'^adm/opcionais/', adminOpcionaisView.as_view(), name="Opcionais-adm"),
    url(r'^adm/opcional-novo', adminOpcionalNovaView.as_view(), name="NovoOpcional-adm"),
    url(r'^adm/opcional-excluir$', adminOpcionalExcluirView.as_view(), name="ExcluirOpcional-adm"),
    url(r'^adm/opcional-ver', adminOpcionalVerView.as_view(), name="VerOpcional-adm"),
    url(r'^adm/opcional-edicao', adminOpcionalEdicaoView.as_view(), name="EdicaoOpcional-adm"),

    url(r'^adm/opcoes/', adminOpcaoView.as_view(), name="Opcao-adm"),
    url(r'^adm/opcao-novo', adminOpcaoNovaView.as_view(), name="NovaOpcao-adm"),
    url(r'^adm/opcao-excluir$', adminOpcaoExcluirView.as_view(), name="ExcluirOpcao-adm"),

    url(r'^adm/pedidos/', adminPedidosView.as_view(), name="Pedidos-adm"),
    url(r'^adm/pedido-nova', adminPedidoNovaView.as_view(), name="NovaPedido-adm"),
    url(r'^adm/pedido-excluir$', adminPedidoExcluirView.as_view(), name="ExcluirPedido-adm"),
    url(r'^adm/pedido-ver', adminPedidoVerView.as_view(), name="VerPedido-adm"),

    url(r'^adm/tiposcozinha/', adminTiposCozinhaView.as_view(), name="TiposCozinhas-adm"),
    url(r'^adm/tipocozinha-nova', adminTipoCozinhaNovaView.as_view(), name="NovaTipoCozinha-adm"),
    url(r'^adm/tipocozinha-excluir$', adminTipoCozinhaExcluirView.as_view(), name="ExcluirTipoCozinha-adm"),
    url(r'^adm/tipocozinha-ver', adminTipoCozinhaVerView.as_view(), name="VerTipoCozinha-adm"),
    url(r'^adm/tipocozinha-edicao', adminTipoCozinhaEdicaoView.as_view(), name="EdicaoTipoCozinha-adm"),

    url(r'^adm/repasse-atual', adminRepassesAtualView.as_view(), name="Repasses-adm"),
    url(r'^adm/repasses/', adminRepassesView.as_view(), name="Repasses-adm"),
    url(r'^adm/repasse/pagamentos', adminRepassesPagamentosView.as_view(), name="RepassesPagamentos-adm"),
    url(r'^adm/repasse/criar-repasse', adminCriarRepasseView.as_view(), name="CriarRepasse-adm"),
    url(r'^adm/repasse/limitar', adminLimitarEmpresaView.as_view(), name="Limitar-adm"),

    url(r'^js/categorias', ServiceJson.categorias, name='categorias'),
    url(r'^js/clientes', ServiceJson.clientes, name='clientes'),
    url(r'^js/cliente-login', ServiceJson.clienteLogin, name='clientelogin'),
    url(r'^js/cliente-logado', ServiceJson.clienteLogado, name='clientelogado'),
    url(r'^js/cliente-face-login', ServiceJson.clienteFaceLogin, name='clientefacelogin'),
    url(r'^js/subcategorias', ServiceJson.subcategorias, name='subcategorias'),
    url(r'^js/estados', ServiceJson.estados, name='estados'),
    url(r'^js/cidades', ServiceJson.cidades, name='Cidades'),
    url(r'^js/bairros', ServiceJson.bairros, name='bairros'),
    url(r'^js/empresas$', ServiceJson.empresas, name='empresas'),
    url(r'^js/empresaslogotipos$', ServiceJson.empresaslogotipos, name='empresaslogotipos'),
    url(r'^js/empresasavaliacoes$', ServiceJson.empresasavaliacoes, name='empresasavaliacoes'),
    url(r'^js/empresasrepasses', ServiceJson.empresasrepasses, name='empresasrepasses'),
    url(r'^js/empresa-login', ServiceJson.empresaLogin, name='empresaLogin'),
    url(r'^js/funcionarios', ServiceJson.funcionarios, name='funcionarios'),
    url(r'^js/funcionario-login', ServiceJson.funcionarioLogin, name='funcionariologin'),
    url(r'^js/produtos', ServiceJson.produtos, name='produtos'),
    url(r'^js/cardapio', ServiceJson.cardapio, name='cardapio'),
    url(r'^js/pedidos', ServiceJson.pedidos, name='pedidos'),
    url(r'^js/tiposcozinhas', ServiceJson.tiposcozinhas, name='tiposcozinhas'),
    url(r'^js/tipostempo', ServiceJson.tipostempo, name='tipostempo'),
    url(r'^js/itens', ServiceJson.itens, name='itens'),
    url(r'^js/carrinho', ServiceJson.carrinho, name='carrinho'),
    url(r'^js/bandeiras', ServiceJson.bandeiras, name='bandeiras'),
    url(r'^js/repasses', ServiceJson.repasses, name='repasses'),
    url(r'^js/mensalidades', ServiceJson.mensalidades, name='mensalidades'),
    url(r'^js/opcionais', ServiceJson.opcionais, name='opcionais'),
    url(r'^js/opcoes', ServiceJson.opcoes, name='opcoes'),
    # url(r'^js/tipospagamentos', ServiceJson.tipospagamentos, name='tipospagamentos'),


    url(r'^js/saveopcional', ServiceJson.saveopcional, name='saveopcional'),
    url(r'^js/saveopcao', ServiceJson.saveopcao, name='saveopcao'),
    url(r'^js/saveavaliacao', ServiceJson.saveavaliacao, name='saveavaliacao'),
    url(r'^js/savecategoria', ServiceJson.savecategoria, name='savecategoria'),
    url(r'^js/savecliente$', ServiceJson.savecliente, name='savecliente'),
    url(r'^js/saveclientehome', ServiceJson.saveclientehome, name='saveclientehome'),
    url(r'^js/savesubcategoria', ServiceJson.savesubcategoria, name='savesubcategoria'),
    url(r'^js/saveprodutosubcategoria$', ServiceJson.saveprodutosubcategoria, name='saveprodutosubcategoria'),
    url(r'^js/saveprodutoopcional', ServiceJson.saveprodutoopcional, name='saveprodutoopcional'),
    url(r'^js/saveestado', ServiceJson.saveestado, name='saveestado'),
    url(r'^js/savecidade', ServiceJson.savecidade, name='savecidade'),
    url(r'^js/savebairro', ServiceJson.savebairro, name='savebairro'),
    url(r'^js/saveempresa$', ServiceJson.saveempresa, name='saveempresa'),
    url(r'^js/saveempresabairro$', ServiceJson.saveempresabairro, name='saveempresabairro'),
    url(r'^js/savefuncionario', ServiceJson.savefuncionario, name='savefuncionario'),
    url(r'^js/saverepasse', ServiceJson.saverepasse, name='saverepasse'),
    url(r'^js/saveproduto', ServiceJson.saveproduto, name='saverproduto'),
    url(r'^js/savepedido$', ServiceJson.savepedido, name='savepedido'),
    url(r'^js/saveitem', ServiceJson.saveitem, name='saveitem'),
    url(r'^js/savetipocozinha', ServiceJson.savetipocozinha, name='savetipocozinha'),
    url(r'^js/savecarrinho', ServiceJson.savecarrinho, name='savecarrinho'),
    url(r'^js/savetipopagamentopedido', ServiceJson.savetipopagamentopedido, name='savetipopagamentopedido'),
    url(r'^js/saveobspagamentopedido', ServiceJson.saveobspagamentopedido, name='saveobspagamentopedido'),
    url(r'^js/savemensalidade', ServiceJson.savemensalidade, name='savemensalidade'),
    url(r'^js/efetuar-pagamento', ServiceJson.efetuarpagamento, name='efetuarpagamento'),
    url(r'^js/savepedidostatus$', ServiceJson.savepedido_status, name='savepedidostatus'),
    url(r'^js/criarrepasse', ServiceJson.criarrepasse, name='criarrepasse'),
    url(r'^js/receberrepasse', ServiceJson.receberrepasse, name='receberrepasse'),
    url(r'^js/settempoentrega', ServiceJson.settempoentrega, name='receberrepasse'),
    url(r'^js/enviarempresa', ServiceJson.enviarempresa, name='enviarempresa'),

    url(r'^js/excluiropcional', ServiceJson.excluiropcional, name='excluiropcional'),
    url(r'^js/excluiropcao', ServiceJson.excluiropcao, name='excluiropcao'),
    url(r'^js/excluircategoria', ServiceJson.excluircategoria, name='excluircategoria'),
    url(r'^js/excluircliente', ServiceJson.excluircliente, name='excluircliente'),
    url(r'^js/excluirsubcategoria', ServiceJson.excluirsubcategoria, name='excluirsubcategoria'),
    url(r'^js/excluirempresa$', ServiceJson.excluirempresa, name='excluirempresa'),
    url(r'^js/excluirempresa_bairro$', ServiceJson.excluirempresa_bairro, name='excluirempresa_bairro'),
    url(r'^js/excluirprodutosubcategoria$', ServiceJson.excluirproduto_categoria, name='excluirproduto_categoria'),
    url(r'^js/excluirprodutoopcional$', ServiceJson.excluirproduto_opcional, name='excluirproduto_opcional'),
    url(r'^js/excluirfuncionario', ServiceJson.excluirfuncionario, name='excluirfuncionario'),
    url(r'^js/excluirrepasse', ServiceJson.excluirrepasse, name='excluirrepasse'),
    url(r'^js/excluirproduto$', ServiceJson.excluirproduto, name='excluirproduto'),
    url(r'^js/excluirpedido', ServiceJson.excluirpedido, name='excluirpedido'),
    url(r'^js/excluirtipocozinha', ServiceJson.excluirtipocozinha, name='excluirtipocozinha'),
    url(r'^js/excluircarrinho', ServiceJson.excluircarrinho, name='excluircarrinho'),
    url(r'^js/excluirmensalidade', ServiceJson.excluirmensalidade, name='excluirmensalidade'),

    url(r'^js/abrirempresa', ServiceJson.abrirempresa, name='abrirempresa'),
    url(r'^js/fecharempresa', ServiceJson.fecharempresa, name='fecharempresa'),
    url(r'^js/getabertura$', ServiceJson.getabertura, name='getabertura'),
    url(r'^js/getrestaurantes$', ServiceJson.getRestaurantes, name='getRestaurantes'),
    url(r'^js/getrestaurantesbairro', ServiceJson.getRestaurantesBairro, name='getRestaurantesBairro'),
    url(r'^js/getrestaurantebypedido', ServiceJson.getrestaurantebypedido, name='getrestaurantebypedido'),
    url(r'^js/getaberturas$', ServiceJson.getaberturas, name='getaberturas'),
    url(r'^js/esqueceusenha_cliente', ServiceJson.esqueceusenhacliente, name='esqueceusenha_cliente'),
    url(r'^js/recuperar_cliente', ServiceJson.recuperarsenhacliente, name='recuperarsenhacliente'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
