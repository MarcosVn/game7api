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

game7App.controller('clienteCtrl', function($scope, Cliente, Estado, Cidade, Bairro, Funcionario) {
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
});

game7App.controller('empresaCtrl', function($scope, Empresa, Estado, Cidade, Bairro, Atendimento, Funcionario, TipoCozinha) {
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
            document.getElementById("porcentagem_repasse").value);
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

game7App.controller('produtoCtrl', function($scope, Produto, Empresa, Categoria, SubCategoria, Funcionario) {
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

    $scope.filtrar = function(){
        $scope.pt.get_produtos(document.getElementById("ipFiltroNome").value);
    }
    $scope.atualizar = function(){
        $scope.pt.save_produto(
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
    $scope.atualizar_produtocategoria = function(){
        $scope.pt.save_produtocategoria($scope.sc.sel_subcategorias.pk);
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