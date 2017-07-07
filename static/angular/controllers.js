game7App.controller('categoriaCtrl', function($scope, Categoria, Funcionario) {
    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.ct = Categoria;
    $scope.ct.get_categorias();
    $scope.ct.get_categoria();
    $scope.filtrar = function(){
        $scope.ct.get_categorias(document.getElementById("ipFiltroCategoria").value);
    }
    $scope.atualizar = function(){
        $scope.ct.save_categoria(document.getElementById("nome").value);
    }
    $scope.excluir = function(){
      $scope.ct.excluir_categoria();
    }
});

game7App.controller('subcategoriaCtrl', function($scope, SubCategoria, Categoria, Funcionario) {
    $scope.fn = Funcionario;
    $scope.fn.verifica_login();
    $scope.sc = SubCategoria;
    $scope.ct = Categoria;
    $scope.ct.get_categoria();
    $scope.sc.get_subcategorias();
    $scope.sc.get_subcategoria();
    $scope.filtrar = function(){
        $scope.sc.get_subcategorias(document.getElementById("ipFiltroSubCategoria").value);
    }
    $scope.atualizar = function(){
        $scope.sc.save_subcategoria(document.getElementById("nome").value);
    }
    $scope.excluir = function(){
      $scope.sc.excluir_subcategoria();
    }
});

game7App.controller('clienteCtrl', function($scope,$http, Cliente, Estado, Cidade, Bairro, Funcionario) {
    enderecocep = [];

    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.et = Estado;
    $scope.et.get_estados();

    $scope.cd = Cidade;

    $scope.br = Bairro;

    $scope.cl = Cliente;
    $scope.cl.get_cliente();
    $scope.cl.get_clientes();
    $scope.filtrar = function(){
        $scope.cl.get_clientes(document.getElementById("ipFiltroNome").value,document.getElementById("ipFiltroEmail").value);
    }
    $scope.atualizar = function(){
        $scope.cl.save_cliente(
            document.getElementById("nome").value,
            document.getElementById("email").value,
            document.getElementById("senha").value,
            document.getElementById("telefone").value,
            document.getElementById("estado").value,
            document.getElementById("cidade").value,
            document.getElementById("bairro").value,
            document.getElementById("endereco").value,
            document.getElementById("numero").value,
            document.getElementById("complemento").value,
            document.getElementById("cep").value
            );
    }
    $scope.excluir = function(){
      $scope.cl.excluir_cliente();
    }
    $scope.getcidades = function(){
        $scope.cd.get_cidades(document.getElementById("estado").value);
    }
    $scope.getbairros = function(){
        $scope.br.get_bairros(document.getElementById("cidade").value);
    }
    $scope.getcep = function(){
        cep = $("#cep").val();
        //Get relação de clientes
        var url = "http://viacep.com.br/ws/"+ cep + "/json/";
        var params = {
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            enderecocep = response.data;

            //Endereco
            $("#endereco").val(enderecocep.logradouro);

            //Estado
            if(enderecocep.uf = "SP"){
                $("#estado").val("1");
            }

            //Cidade
            $scope.cd.get_cidades($("#estado").val());
            $scope.cd.get_cidades_by_nome(enderecocep.cidade);

            //Bairro
            $scope.br.get_bairros($scope.cd.cidade_selecionado.id);
            $scope.br.get_bairros_by_nome(enderecocep.bairro);




        }, function errorCallback(response) {
            console.log("Erro");
        });
    }

});

game7App.controller('empresaCtrl', function($scope,$http, Empresa, Estado, Cidade, Bairro, Atendimento, Funcionario, TipoCozinha) {
    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.et = Estado;
    $scope.cd = Cidade;
    $scope.br = Bairro;
    $scope.em = Empresa;
    $scope.at = Atendimento;
    $scope.tc = TipoCozinha;

    $scope.et.get_estados();
    $scope.tc.get_tiposcozinha();
    $scope.em.get_empresas();
    $scope.em.get_empresa();


    $scope.filtrar = function(){
        $scope.em.get_empresas(document.getElementById("ipFiltroNome").value,document.getElementById("ipFiltroEmail").value);
    }
    $scope.atualizar = function(){

        $scope.em.save_empresa(
            document.getElementById("nome").value,
            document.getElementById("email").value,
            document.getElementById("senha").value,
            document.getElementById("telefone").value,
            document.getElementById("estado").value,
            document.getElementById("cidade").value,
            document.getElementById("bairro").value,
            document.getElementById("endereco").value,
            document.getElementById("descricao").value,
            document.getElementById("tipocozinha").value,
            document.getElementById("valor_mensalidade").value,
            document.getElementById("porcentagem_repasse").value,
            document.getElementById("numero").value,
            document.getElementById("complemento").value,
            document.getElementById("cep").value
            );
    }
    $scope.excluir = function(){
      $scope.em.excluir_empresa();
    }
    $scope.getcidades = function(){
        $scope.cd.get_cidades(document.getElementById("estado").value);
    }
    $scope.getbairros = function(){
        $scope.br.get_bairros(document.getElementById("cidade").value);
    }
    $scope.atualizar_atendimento = function(){
        $scope.at.save_atendimento(
            document.getElementById("bairro").value,document.getElementById("frete").value);
    }
    $scope.excluir_atendimento = function(){
        $scope.at.excluir_atendimento();
    }
    $scope.getcep = function(){
        cep = $("#cep").val();
        //Get relação de clientes
        var url = "http://viacep.com.br/ws/"+ cep + "/json/";
        var params = {
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            enderecocep = response.data;

            //Endereco
            $("#endereco").val(enderecocep.logradouro);

            //Estado
            if(enderecocep.uf = "SP"){
                $("#estado").val("1");
            }

            //Cidade
            $scope.cd.get_cidades($("#estado").val());
            $scope.cd.get_cidades_by_nome(enderecocep.cidade);

            //Bairro
            $scope.br.get_bairros($scope.cd.cidade_selecionado.id);
            $scope.br.get_bairros_by_nome(enderecocep.bairro);




        }, function errorCallback(response) {
            console.log("Erro");
        });
    }
});

game7App.controller('empresarepasseCtrl', function($scope, Empresa, Funcionario) {
    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.em = Empresa;
    $scope.em.get_empresarepasse();

    $scope.filtrar = function(){
        $scope.em.get_empresarepasse($('#ipFiltroData').val());

    }
    $scope.efetuarpagamento = function(){
        $scope.em.efetuarrepasse(document.getElementById("ipReferencia").value, $('#ipFiltroData').val());
    }

    $scope.efetuarlimitacao = function(){
        $scope.em.efetuarlimitacao(document.getElementById("ipReferencia").value, $('#ipFiltroData').val());
    }
    $scope.receberrepasse = function(rep_id){
        $scope.em.receberrepasse(rep_id);
        window.location = "/adm/repasse-atual/";
    }
});

game7App.controller('funcionarioCtrl', function($scope, Funcionario) {
    $scope.fn = Funcionario;
    $scope.fn.get_funcionarios();
    $scope.fn.get_funcionario();
    $scope.fn.verifica_login();

    $scope.filtrar = function(){
        $scope.fn.get_funcionarios(document.getElementById("ipFiltroNome").value,document.getElementById("ipFiltroEmail").value);
    }
    $scope.atualizar = function(){
        $scope.fn.save_funcionario(
            document.getElementById("nome").value,
            document.getElementById("email").value,
            document.getElementById("senha").value,
            document.getElementById("telefone").value,
            document.getElementById("endereco").value);
    }
    $scope.excluir = function(){
      $scope.fn.excluir_funcionario();
    }

    $scope.sair = function(){
      $scope.fn.sair();
    }
});

game7App.controller('produtoCtrl', function($scope, Produto, Empresa, Categoria, SubCategoria, Funcionario, Opcional) {
    $scope.em = Empresa;
    $scope.em.get_empresas();

    $scope.pt = Produto;
    $scope.pt.get_produtos();
    $scope.pt.get_produto();

    $scope.ct = Categoria;
    $scope.ct.get_categorias();

    $scope.sc = SubCategoria;

    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.op = Opcional;
    $scope.op.get_opcionais();

    $scope.filtrar = function(){
        $scope.pt.get_produtos(document.getElementById("ipFiltroNome").value, document.getElementById("ipFiltroRestaurante").value);
    }
    $scope.atualizar = function(){
        if($scope.sc.sel_subcategorias){
            $scope.pt.save_produto(
                document.getElementById("nome").value,
                document.getElementById("preco").value,
                document.getElementById("descricao").value,
                document.getElementById("empresa").value,
                $scope.sc.sel_subcategorias.pk
                );
        }
        else{
            $scope.pt.save_produto(
                document.getElementById("nome").value,
                document.getElementById("preco").value,
                document.getElementById("descricao").value,
                document.getElementById("empresa").value,
                ''
                );
        }
    }
    $scope.excluir = function(){
      $scope.pt.excluir_produto();
    }
    $scope.getsubs= function(){
        $scope.sc.get_subcategorias("",$scope.sc.sel_categoria.pk);
    }
    $scope.atualizar_produtocategoria = function(){
        $scope.pt.save_produtocategoria($scope.sc.sel_subcategorias.pk);
    }
    $scope.atualizar_produtoopcional = function(){
        $scope.pt.save_produtoopcional($scope.op.sel_opcional.id);
    }
    $scope.excluir_produtoopcional = function(){
        $scope.pt.excluir_produtoopcional();
    }
    $scope.excluir_produtocategoria = function(){
        $scope.pt.excluir_produtocategoria();
    }
    $scope.atualizar_produtofoto = function(){
        $scope.pt.save_produtofoto();
        $scope.pt.get_produto();
        location.reload();
    }
    $scope.excluir_produtofoto = function(foto_id){
        $scope.pt.excluir_produtofoto(foto_id);
        location.reload();
    }
});

game7App.controller('pedidoCtrl', function($scope, Pedido, Empresa, Funcionario) {
    $scope.em = Empresa;
    $scope.em.get_empresas();

    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

    $scope.pe = Pedido;
    $scope.pe.get_pedidos();

    $scope.filtrar = function(){
        $scope.pe.get_pedidos($("#ipFiltrodata").val(),$("#selStatus").val());
    }
    $scope.atualizar = function(){
        $scope.pe.save_pedido(
            document.getElementById("nome").value,
            document.getElementById("preco").value,
            document.getElementById("descricao").value,
            document.getElementById("empresa").value);
    }
    $scope.excluir = function(){
      $scope.pt.excluir_produto();
    }
    $scope.getsubs= function(){
        $scope.sc.get_subcategorias("",$scope.sc.sel_categoria.pk);
    }
});

game7App.controller('loginCtrl', function($scope, Funcionario, Cliente) {
    $scope.lg = Funcionario;
    $scope.cl = Cliente;
    $scope.logar = function(){
        $scope.lg.logar_funcionario(document.getElementById("ipEmail").value,document.getElementById("ipSenha").value);
    }
    $scope.recuperarsenha = function(){
        if(document.getElementById("ipSenha").value == document.getElementById("ipSenhaConfirmar").value){
            $scope.cl.get_recuperarsenha(document.getElementById("ipEmail").value, document.getElementById("ipSenha").value);
        }
        else
        {
            alert("As senhas precisam ser iguais.");
        }

    }

});

game7App.controller('tiposcozinhasCtrl', function($scope, TipoCozinha) {
    $scope.tc = TipoCozinha;
    $scope.tc.get_tiposcozinha();
    $scope.tc.get_tipocozinha();

    $scope.filtrar = function(){
        $scope.tc.get_tiposcozinha(document.getElementById("ipFiltroTipoCozinha").value);
    }
    $scope.atualizar = function(){
        $scope.tc.save_tipocozinha(document.getElementById("nome").value);
    }
    $scope.excluir = function(){
      $scope.tc.excluir_tipocozinha();
    }
});

game7App.controller('mensalidadesCtrl', function($scope, Mensalidade) {
    $scope.ms = Mensalidade;
    $scope.ms.get_mensalidades();

    $scope.filtrar = function(){
        $scope.ms.get_mensalidades($("#ipFiltroData").val(),$("#selStatus").val());
    }
    $scope.gerarmensalidade = function(id){
        $scope.ms.gerar_mensalidade(id);
    }
    $scope.recebermensalidade = function(id){
        $scope.ms.receber_mensalidade(id);
    }
    $scope.cancelar = function(id){
      $scope.ms.cancelar_mensalidade(id);
    }
});

game7App.controller('opcionalCtrl', function($scope, Opcional, Empresa) {
    $scope.op = Opcional;
    $scope.op.get_opcionais();
    $scope.op.get_opcional();

    $scope.em = Empresa;
    $scope.em.get_empresas();

    $scope.filtrar = function(){
        $scope.op.get_opcionais(document.getElementById("ipFiltroTitulo").value);
    }
    $scope.atualizar = function(){
        alert(document.getElementById("empresa").value);
        alert(document.getElementById("titulo").value);
        alert(document.getElementById("quantidade").value);
        alert(document.getElementById("tipo").value);
        $scope.op.save_opcional(
            document.getElementById("empresa").value,
            document.getElementById("titulo").value,
            document.getElementById("quantidade").value,
            document.getElementById("tipo").value);
    }
    $scope.excluir = function(){
      $scope.op.excluir_opcional();
    }
});

game7App.controller('opcaoCtrl', function($scope, Opcional, Opcao) {
    $scope.op = Opcional;
    $scope.op.get_opcionais();
    $scope.op.get_opcional();


    $scope.oa = Opcao;
    $scope.oa.get_opcoes();
    $scope.oa.get_opcao();

    $scope.filtrar = function(){
        $scope.oa.get_opcoes(document.getElementById("ipFiltroTitulo").value);
    }
    $scope.atualizar = function(){
        $scope.oa.save_opcao(
            document.getElementById("titulo").value,
            document.getElementById("valor").value);
    }
    $scope.excluir = function(){
      $scope.oa.excluir_opcao();
    }
});



game7App.controller('topoCtrl', function($scope, $http, Cliente, Estado, Cidade, Bairro) {
    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();

    $scope.et = Estado;
    $scope.cd = Cidade;
    $scope.br = Bairro;

    $scope.et.get_estados();

    $scope.efetuarlogar = function(){
        $scope.cl.logar_cliente(
            document.getElementById("loginemail").value,
            document.getElementById("loginsenha").value);
    }
    $scope.sair= function(){
        $scope.cl.sair_cliente();
    }
    $scope.atualizar = function(){
        $scope.cl.save_cliente(
            document.getElementById("nome").value,
            document.getElementById("email").value,
            document.getElementById("senha").value,
            document.getElementById("telefone").value,
            document.getElementById("estado").value,
            document.getElementById("cidade").value,
            document.getElementById("bairro").value,
            document.getElementById("endereco").value,
            document.getElementById("numero").value,
            document.getElementById("complemento").value,
            document.getElementById("cep").value
            );
    }
    $scope.getcep = function(){
        cep = $("#cep").val();
        //Get relação de clientes
        var url = "http://viacep.com.br/ws/"+ cep + "/json/";
        var params = {
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            enderecocep = response.data;

            //Endereco
            $("#endereco").val(enderecocep.logradouro);

            //Estado
            if(enderecocep.uf = "SP"){
                $("#estado").val("1");
            }

            //Cidade
            $scope.cd.get_cidades($("#estado").val());
            $scope.cd.get_cidades_by_nome(enderecocep.cidade);

            //Bairro
            $scope.br.get_bairros($scope.cd.cidade_selecionado.id);
            $scope.br.get_bairros_by_nome(enderecocep.bairro);




        }, function errorCallback(response) {
            console.log("Erro");
        });
    }
});

game7App.controller('restauranteloginCtrl', function($scope, Empresa) {
    $scope.em = Empresa;

    $scope.logar = function(){
        $scope.em.logar_empresa(
            document.getElementById("ipEmail").value,
            document.getElementById("ipSenha").value);
    }
})

game7App.controller('topoRestauranteCtrl', function($scope, Empresa) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.verifica_login();

    $scope.sair= function(){
        $scope.em.sair_empresa();
    }
});

game7App.controller('homeRestauranteCtrl', function($scope, Empresa, TipoTempo, Pedido) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.get_empresalogadorepasse();
    $scope.em.verifica_login();

    $scope.tt = TipoTempo;
    $scope.tt.get_tipostempo();

    $scope.pe = Pedido;
    $scope.pe.get_pedidos_status('Aguardando Aprovacao');


    $scope.sair= function(){
        $scope.em.sair_empresa();
    }

    $scope.set_tempoentrega = function(){
        $scope.em.set_tempoentrega($('#selTempoEntrega').val());
    }

    $scope.abriredicaotempo = function(){
        $('#temposelecionado').hide();
        $('#temposelecionar').show();
    }

    $scope.atualizar_status = function(pedido_id, status_valor){
        $scope.pe.save_pedido_status(
            pedido_id,
            status_valor
        );

        $scope.pe.get_pedidos_status('Aguardando Aprovacao');
    }
});

game7App.controller('perfilRestauranteCtrl', function($scope, Empresa) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.verifica_login();

    $scope.atualizar = function(){

        $scope.em.atualizar_perfil_empresa(
            document.getElementById("telefone").value,
            document.getElementById("endereco").value,
            document.getElementById("descricao").value,
            $('input[name="aceita_cartao"]:checked').val(),
            $('input[name="aceita_valerefeicao"]:checked').val(),
            $('input[name="aceita_pagamentoonline"]:checked').val());
    }
});

game7App.controller('expedienteRestauranteCtrl', function($scope, Empresa) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.verifica_login();
    $scope.em.get_abertura();
    $scope.em.get_aberturas();

    $scope.abrir_empresa = function(){
        $scope.em.abrir_empresa();
    }
    $scope.fechar_empresa = function(abertura_id){
        $scope.em.fechar_empresa(abertura_id);
        window.location="/restaurante/expediente";
    }
});

game7App.controller('cardapioRestauranteCtrl', function($scope, Empresa, Produto) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.verifica_login();

    $scope.pt = Produto;
    $scope.pt.get_produtos_restaurante("");

});


game7App.controller('cardapioRestauranteNovoCtrl', function($scope, Empresa, Produto, Categoria, SubCategoria, Opcional) {
    $scope.em = Empresa;
    $scope.em.get_empresalogado();
    $scope.em.verifica_login();

    $scope.ct = Categoria;
    $scope.ct.get_categorias();

    $scope.sc = SubCategoria;
    $scope.pt = Produto;

    $scope.pt = Produto;
    $scope.pt.get_produtos();
    $scope.pt.get_produto();

    $scope.ct = Categoria;
    $scope.ct.get_categorias();

    $scope.sc = SubCategoria;

    $scope.op = Opcional;
    $scope.op.get_opcionais();

    $scope.filtrar = function(){
        $scope.pt.get_produtos(document.getElementById("ipFiltroNome").value, document.getElementById("ipFiltroRestaurante").value);
    }
    $scope.atualizar = function(){
        if($scope.sc.sel_subcategorias){
            $scope.pt.save_produto(
                document.getElementById("nome").value,
                document.getElementById("preco").value,
                document.getElementById("descricao").value,
                window.localStorage.getItem("e_logado"),
                $scope.sc.sel_subcategorias.pk
                );
        }
        else{
            $scope.pt.save_produto(
                document.getElementById("nome").value,
                document.getElementById("preco").value,
                document.getElementById("descricao").value,
                window.localStorage.getItem("e_logado"),
                ''
                );
        }
    }
    $scope.excluir = function(){
      $scope.pt.excluir_produto();
    }
    $scope.getsubs= function(){
        $scope.sc.get_subcategorias("",$scope.sc.sel_categoria.pk);
    }
    $scope.atualizar_produtocategoria = function(){
        $scope.pt.save_produtocategoria($scope.sc.sel_subcategorias.pk);
    }
    $scope.atualizar_produtoopcional = function(){
        $scope.pt.save_produtoopcional($scope.op.sel_opcional.id);
    }
    $scope.excluir_produtoopcional = function(){
        $scope.pt.excluir_produtoopcional();
    }
    $scope.excluir_produtocategoria = function(){
        $scope.pt.excluir_produtocategoria();
    }
    $scope.atualizar_produtofoto = function(){
        $scope.pt.save_produtofoto();
        $scope.pt.get_produto();
        location.reload();
    }
    $scope.excluir_produtofoto = function(foto_id){
        $scope.pt.excluir_produtofoto(foto_id);
        location.reload();
    }

});

game7App.controller('repasseRestauranteCtrl', function($scope, Empresa) {
    $scope.em = Empresa;
    $scope.em.get_empresalogadorepasse();

    $scope.filtrar = function(){
        $scope.em.get_empresarepasse($('#ipFiltroData').val());
    }
    $scope.efetuarpagamento = function(){
        $scope.em.efetuarrepasse(document.getElementById("ipReferencia").value, $('#ipFiltroData').val());
    }
});


game7App.controller('pedidosRestauranteCtrl', function($scope, Empresa, Pedido) {
    $scope.em = Empresa;
    $scope.em.get_empresalogadorepasse();

    $scope.pe = Pedido;

    $scope.pe.get_pedidos_agpreparo();
    $scope.pe.get_pedidos_empreparo();
    $scope.pe.get_pedidos_agentrega();
    $scope.pe.get_pedidos_concluido();

    $scope.filtrar = function(){
        $scope.pe.get_pedidos(document.getElementById("ipFiltrodata").value);
    }

    $scope.filtrar_status = function(status){
        $scope.pe.get_pedidos_status(status);
    }

    $scope.filtrar_status_agentrega = function(){
        $scope.pe.get_pedidos_agentrega();
    }

    $scope.filtrar_status_agpreparo = function(){
        $scope.pe.get_pedidos_agpreparo();
    }

    $scope.filtrar_status_empreparo = function(){
        $scope.pe.get_pedidos_empreparo();
    }

    $scope.filtrar_status_concluido = function(){
        $scope.pe.get_pedidos_concluido();
    }

    $scope.atualizar_status = function(status,pedido_id){
        $scope.pe.save_pedido_status(pedido_id,status);
    }

    $scope.atualizar = function(){
        $scope.pe.save_pedido(
            document.getElementById("nome").value,
            document.getElementById("preco").value,
            document.getElementById("descricao").value,
            window.localStorage.getItem("e_logado"));
    }

    $scope.filtrar = function(){
        $scope.em.get_empresarepasse($('#ipFiltroData').val());

    }
    $scope.efetuarpagamento = function(){
        $scope.em.efetuarrepasse(document.getElementById("ipReferencia").value, $('#ipFiltroData').val());
    }
});

game7App.controller('avaliacoesRestauranteCtrl', function($scope, Empresa, Pedido) {
    $scope.em = Empresa;
//    $scope.em.get_empresalogadorepasse();
});


game7App.controller('atendimentoRestauranteCtrl', function($scope, Empresa, Estado, Cidade, Bairro, Atendimento) {
    $scope.et = Estado;
    $scope.cd = Cidade;
    $scope.br = Bairro;
    $scope.em = Empresa;
    $scope.at = Atendimento;

    $scope.et.get_estados();

    $scope.getcidades = function(){
        $scope.cd.get_cidades(document.getElementById("estado").value);
    }
    $scope.getbairros = function(){
        $scope.br.get_bairros(document.getElementById("cidade").value);
    }
    $scope.atualizar_atendimento = function(){
        $scope.at.save_restaurante_atendimento(
            document.getElementById("bairro").value,
            document.getElementById("frete").value);
    }
    $scope.excluir_atendimento = function(){
        $scope.at.excluir_restaurante_atendimento();
    }
});