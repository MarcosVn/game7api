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

    $scope.fn = Funcionario;
    $scope.fn.verifica_login();

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
        $scope.op.save_opcional(
            document.getElementById("empresa").value,
            document.getElementById("titulo").value,
            $('input[name="quantitativo"]:checked').val(),
            $('input[name="unico"]:checked').val());
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