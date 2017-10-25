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
        //Get relaÃ§Ã£o de clientes
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
        //Get relaÃ§Ã£o de clientes
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



game7App.controller('topoCtrl', function($scope, $http, Cliente, Estado, Cidade, Bairro, TipoCozinha, Empresa) {
    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();

    $scope.et = Estado;
    $scope.cd = Cidade;
    $scope.br = Bairro;
    $scope.tc = TipoCozinha;
    $scope.em = Empresa;

    $scope.et.get_estados();
    $scope.tc.get_tiposcozinha();

    $scope.cadastraremail = function(){
        console.log("enviando a conclusao dos itens de home");
        $("#gencadastroemail").show();
    }

    $scope.efetuarlogar = function(){
        $scope.cl.logar_cliente(
            document.getElementById("loginemail").value,
            document.getElementById("loginsenha").value);
    }
    $scope.logarfacebook = function(nome, f_id){
        $scope.cl.logarfacebook(nome, f_id);
    }
    $scope.sair= function(){
        $scope.cl.sair_cliente();
    }
    $scope.atualizar = function(){
        $scope.cl.save_cliente_home(
            document.getElementById("nome").value,
            document.getElementById("email").value,
            document.getElementById("senha").value,
            document.getElementById("telefone").value
//            document.getElementById("estado").value,
//            document.getElementById("cidade").value,
//            document.getElementById("bairro").value,
//            document.getElementById("endereco").value,
//            document.getElementById("numero").value,
//            document.getElementById("complemento").value,
//            document.getElementById("cep").value
            );
    }
    $scope.atualizarrestaurante = function(){
        $scope.em.enviar_empresa(
            document.getElementById("restaurantenome").value,
            document.getElementById("restauranteemail").value,
            document.getElementById("restaurantetelefone").value,
            document.getElementById("restauranteresponsavel").value,
            document.getElementById("restauranteestado").value,
            document.getElementById("restaurantecidade").value,
            document.getElementById("restaurantebairro").value,
            document.getElementById("restauranteendereco").value,
            document.getElementById("restaurantenumero").value,
            document.getElementById("restaurantecomplemento").value,
            document.getElementById("restaurantecep").value,
            document.getElementById("restaurantetipocozinha").value
            );
    }
    $scope.getcep = function(){
        cep = $("#cep").val();
        //Get relaÃ§Ã£o de clientes
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

    $scope.getceprestaurante = function(){
        cep = $("#restaurantecep").val();
        //Get relaÃ§Ã£o de clientes
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
            $("#restauranteendereco").val(enderecocep.logradouro);

            //Estado
            if(enderecocep.uf = "SP"){
                $("#restauranteestado").val("1");
            }

            //Cidade
            $scope.cd.get_cidades($("#restauranteestado").val());
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

    $scope.imprimir_pedido = function(pedido_id){
        gen_pedido = $("#ped_"+pedido_id);

        console.log(gen_pedido.html());

        var mywindow = window.open('', 'PRINT', 'height=400,width=600');

        mywindow.document.write("<html><head><title>" + document.title  + "</title>");
        mywindow.document.write("</head><body style='font-family:Arial;font-size:12px;list-style:none;'>");
        mywindow.document.write("<h1>" + document.title  + "</h1>");
        mywindow.document.write("<div style='border:1px solid #fff;width:400px;'>" + gen_pedido.html() + "</div>");
        mywindow.document.write("</body></html>");

        mywindow.document.close(); // necessary for IE >= 10
        mywindow.focus(); // necessary for IE >= 10*/

        mywindow.print();
        mywindow.close();

        return true;
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

game7App.controller('topoClienteCtrl', function($scope, Cliente, Pedido ) {
    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();
    $scope.sair= function(){
        $scope.cl.sair_cliente();
    }

    $scope.pe = Pedido;
    $scope.pe.get_pedidos_concluido_cliente();
//    $scope.em.get_empresalogadorepasse();

    $scope.set_avaliacao_pedido = function(nota, pedido_id){
        $scope.pe.save_avaliacao(nota,pedido_id,$('#ipMensagem'+pedido_id).val());
    }
});

game7App.controller('homeClienteCtrl', function($scope, Cliente, Empresa) {
    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();

    $scope.em = Empresa;
    $scope.em.get_empresas_buscas();
//
    if(document.getElementById('iFiltro').value != ""){
        $scope.em.get_empresas(document.getElementById('iFiltro').value);
    }

    $scope.set_tipocozinha = function(nTipoCozinha){
        $scope.em.set_tipocozinha(nTipoCozinha);

        $scope.filtrar();
    }

    $scope.filtrar = function(){
        $scope.em.get_empresas_buscas(document.getElementById('iFiltro').value);
    }

//    $scope.em.get_empresalogadorepasse();
});

game7App.controller('perfilClienteCtrl', function($scope, $http, Cliente, Estado, Cidade, Bairro) {
    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();

    enderecocep = [];

    $scope.et = Estado;
    $scope.et.get_estados();

    $scope.cd = Cidade;

    $scope.br = Bairro;
    $scope.getcidades = function(){
        $scope.cd.get_cidades(document.getElementById("estado").value);
    }
    $scope.getbairros = function(){
        $scope.br.get_bairros(document.getElementById("cidade").value);
    }
    $scope.getcep = function(){
        cep = $("#cep").val();
        //Get relaÃ§Ã£o de clientes
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
            $scope.et.get_estados();
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

    $scope.atualizar = function(){
        $scope.cl.save_logado_cliente(
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
});


game7App.controller('pedidosClienteCtrl', function($scope, Pedido) {
    $scope.pe = Pedido;
    $scope.pe.get_pedidos_logado();
//    $scope.em.get_empresalogadorepasse();

    $scope.filtrar_pedido = function(){
        $scope.pe.filtrar_pedidos_logado($('#data').val(), $('#selStatus').val());
    }

});


game7App.controller('restauranteintegraClienteCtrl', function($scope, Empresa, Produto) {
    $scope.em = Empresa;
    $scope.em.get_empresa();

    $scope.pt = Produto;
    $scope.pt.get_cardapio();

//    $scope.em.get_empresalogadorepasse();
    $scope.filtrar_produtos = function(){
        $scope.pt.get_cardapio($('#filtro_sub').val(),$('#filtroprato').val());

    }
});

game7App.controller('carrinhoCtrl', function($scope, Produto, Carrinho, Pedido) {
    $scope.pe = Pedido;
    $scope.pt = Produto;
//    $scope.pt.get_produtos();
    $scope.pt.get_produto();

    $scope.cr = Carrinho;
    $scope.cr.get_carrinhos();

    $scope.fechar_pedido = function(){

        if ($scope.cr.lista_compra.length > 0){
            $scope.pe.save_pedido_logado("?", "?", "?", "?");
            //window.location = "/cliente/realizarpedido/endereco";
        }
        else{
            alert("Por favor, adicione pelo menos um produto.");
        }

    }

    $scope.add_opcao_quantidade = function(opcional_id, opcao_id){
        for (x = 0; x < $scope.pt.produtoselecionado[0].opcionais.length; x++){
            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_id == opcional_id){
                for (y = 0; y < $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes.length; y++){
                    if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_id == opcao_id){
                        if($scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade_selecionado < $scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade){
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade ++;
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = true;
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade_selecionado ++;
                        }
                        else{
                            alert("VocÃª jÃ¡ atingiu o limite de opcionais");
                        }
                    }
                }
            }
        }
    }

    $scope.rm_opcao_quantidade = function(opcional_id, opcao_id){
        for (x = 0; x < $scope.pt.produtoselecionado[0].opcionais.length; x++){
            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_id == opcional_id){
                for (y = 0; y < $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes.length; y++){
                    if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_id == opcao_id){
                        if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade > 0){
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade --;
                            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade == 0){
                                $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = false;
                            }
                        }
                    }
                }
            }
        }
    }


    $scope.seleciona_opcao_multiplo = function(opcional_id, opcao_id){
        for (x = 0; x < $scope.pt.produtoselecionado[0].opcionais.length; x++){
            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_id == opcional_id){
                for (y = 0; y < $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes.length; y++){
                    if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_id == opcao_id){
                        opc_selecionado = "#opc_" + $scope.pt.produtoselecionado[0].opcionais[x].opcional_id + " #" + $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_id;
                        if($(opc_selecionado)[0].checked){
                            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade_selecionado < $scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade){
                                $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = true;
                                $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade = 1;
                                $scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade_selecionado ++;
                            }
                            else{
                                alert("VocÃª jÃ¡ atingiu o limite de opcionais");
                                $(opc_selecionado)[0].checked = false;
                            }
                        }
                        else{
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = false;
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade = 0;
                            $scope.pt.produtoselecionado[0].opcionais[x].opcional_quantidade_selecionado --;
                        }
                    }
                }
            }
        }
    }

    $scope.seleciona_opcao_unico = function(opcional_id, opcao_id){
        for (x = 0; x < $scope.pt.produtoselecionado[0].opcionais.length; x++){
            if($scope.pt.produtoselecionado[0].opcionais[x].opcional_id == opcional_id){
                for (y = 0; y < $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes.length; y++){
                    $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = false;
                    $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade = 0;

                    if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_id == opcao_id){
                        $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado = true;
                        $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade = 1;
                    }
                }
            }
        }
    }

    $scope.add_quantidade = function(){
        $scope.cr.qtd_atual = $scope.cr.qtd_atual + 1;
    }

    $scope.rm_quantidade = function(){
        if($scope.cr.qtd_atual > 1){
            $scope.cr.qtd_atual = $scope.cr.qtd_atual - 1;
        }
    }

    $scope.add_lista = function(){
        $scope.cr.save_carrinho($scope.pt.produtoselecionado[0].id, $scope.cr.qtd_atual, document.getElementById("ipObservacao").value, $scope.pt.produtoselecionado[0].preco);
    }

    $scope.rm_lista = function(car_id){
        $scope.cr.excluir_carrinho(car_id);
    }

    $scope.getOpcionalSelecionado = function(){

        texto_selecionado = "";

        for (x = 0; x < $scope.pt.produtoselecionado[0].opcionais.length; x++){
            texto_selecionado = texto_selecionado + $scope.pt.produtoselecionado[0].opcionais[x].opcional_titulo + "\n";
            for (y = 0; y < $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes.length; y++){
                if($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_selecionado){
                    texto_selecionado = texto_selecionado +  $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade + " x " + $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_titulo + "\n";
                    $scope.pt.produtoselecionado[0].preco = $scope.pt.produtoselecionado[0].preco + ($scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_quantidade * $scope.pt.produtoselecionado[0].opcionais[x].opcional_opcoes[y].opcao_valor);
                }
            }
            texto_selecionado = texto_selecionado + "\n\n";
        }

        $("#genopcionais").hide();
        $("#gencarrinho").attr("style", "display:block!important;");


        $("#ipObservacao").val(texto_selecionado);
    }
});

game7App.controller('pagamentoCtrl', function($scope, Pedido, Pagamento) {
    $scope.pe = Pedido;
    $scope.pe.get_pedido();

    $scope.pg = Pagamento;
    $scope.pg.get_pagamento();

});

game7App.controller('realizarpedidosCtrl', function($scope, Pedido, Cliente, Estado, Cidade, Bairro, Empresa) {
    $scope.pe = Pedido;
    $scope.pe.get_pedidos_logado();
    $scope.pe.get_pedido();

    $scope.cl = Cliente;
    $scope.cl.get_clientelogado();

    $scope.et = Estado;
    $scope.et.get_estados();

    $scope.cd = Cidade;
    $scope.br = Bairro;
    $scope.em = Empresa;
    $scope.em.get_empresabypedido();
    $scope.tipo_pagamento = "na_entrega_dinheiro";




    $scope.filtrar = function(){
        $scope.pe.get_pedidos(document.getElementById("ipFiltrodata").value);
    }
    $scope.atualizar = function(){
        $scope.pe.save_pedido_logado(
            document.getElementById("endereco").value,
            document.getElementById("cidade").value,
            document.getElementById("bairro").value,
            document.getElementById("complemento").value);


    }
    $scope.atualizar_tipo_pagamento = function(){
        $scope.pe.save_tipo_pagamento(
                $('input[name="rd_pagamento_tipo"]:checked').val()
            );
    }
    $scope.atualizar_pagamento = function(){
            $scope.pe.save_pagamento_obs(
                $('#troco_para').val(),
                $('#outro_cartao').val(),
                $('input[name="cpf_nota"]:checked').val(),
                $('#selbandeira').val(),
                $('#docNumber').val()
            );
    }
    $scope.excluir = function(){
      $scope.pt.excluir_produto();
    }
    $scope.getsubs= function(){
        $scope.sc.get_subcategorias("",$scope.sc.sel_categoria.pk);
    }
    $scope.getcidades = function(){
        $scope.cd.get_cidades(document.getElementById("estado").value);
    }
    $scope.getbairros = function(){
        $scope.br.get_bairros(document.getElementById("cidade").value);
    }

    $scope.pagarmercadopago = function(request){
        $scope.list = [];

        console.log(request);

        if ($scope.text) {
            $scope.list.push(this.text);
            $scope.text = '';
        }
        //http://127.0.0.1:8010/js/efetuar-pagamento

    }
});

game7App.controller('homeCtrl', function($scope, Home, $http, Empresa) {
    $scope.ho = Home;
    $scope.ho.get_avaliacoes();
    $scope.ho.get_logotipos();

    $scope.em = Empresa;

    $scope.buscahome = function(request){
        cep = $("#cephome").val();
        //Get relaÃ§Ã£o de clientes
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
//            alert(enderecocep.bairro);
            window.location="/busca?bairro=" + enderecocep.bairro;

        }, function errorCallback(response) {
            console.log("Erro");
        });
    }
});


game7App.controller('buscaCtrl', function($scope, Empresa) {
    $scope.em = Empresa;
    $scope.em.get_empresas_buscas_home();

    $scope.filtrar = function(){
        $scope.em.get_empresas_buscas(document.getElementById('iFiltro').value);
    }
});