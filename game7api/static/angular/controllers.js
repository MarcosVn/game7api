manager36App.controller('EventosCtrl', function($scope, Ajax) {
  $scope.estado=null;
  $scope.cidade=null;
  $scope.set_cidades = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.cidades=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/getcidadebyestado?estado=" + $scope.estado;

    Ajax.request("GET", url, that, callback_success, callback_error);
  }
});

manager36App.controller('IntegrantesCtrl', function($scope, Ajax) {
  $scope.estado=null;
  $scope.cidade=null;
  $scope.hierarquias=null;
  $scope.situacoes=null;
  $scope.set_cidades = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.cidades=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/getcidadebyestado?estado=" + $scope.estado;

    Ajax.request("GET", url, that, callback_success, callback_error);
  }
  $scope.getintegrantes = function(){
    console.log($scope.ipFiltroNome);
    console.log($scope.ipFiltroApelido);

    var that = $scope;
    var callback_success = function (response) {
        that.listaintegrantes=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/getintegrantes?nome=" + $scope.ipFiltroNome + "&apelido=" + $scope.ipFiltroApelido+"&ss=1";

    Ajax.request("GET", url, that, callback_success, callback_error);
  }
  $scope.getHierarquias = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.listahierarquia=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/hierarquias?h_min=0&h_max=3";

    Ajax.request("GET", url, that, callback_success, callback_error);
  }

  $scope.getSituacoes = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.situacoes=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/situacoes";

    Ajax.request("GET", url, that, callback_success, callback_error);
  }

  $scope.getHierarquias();
  $scope.getSituacoes();
  $scope.getintegrantes();

});


manager36App.controller('ReunioesCtrl', function($scope, Ajax) {
  $scope.iniciado=false;
  $scope.ConfirmarInicio = function(){

    checks_presentes = $(".checkbox_presentes:checked")
    checks_justificados = $(".checkbox_justificados:checked")

    var l_presentes = "0";
    for (i_p=0;i_p < checks_presentes.length;i_p++){

      l_presentes = l_presentes + ", " + checks_presentes[i_p].value
    }

    var l_justificados = "0";
    for (i_j=0;i_j < checks_justificados.length;i_j++){

      l_justificados = l_justificados + ", " + checks_justificados[i_j].value
    }

    var that = $scope;
    var callback_success = function (response) {
        that.retorno=response.data;
        $scope.iniciado=true;
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/secretaria/reunioes/salvar?datahora=" + $scope.dta + "&secretario=" + $scope.secretario+"&presidido=" + $scope.presidido + "&l_p="+l_presentes+"&l_j="+l_justificados;

    Ajax.request("GET", url, that, callback_success, callback_error);
  }

  $scope.AdicionarAssunto = function(){

    var that = $scope;
    var callback_success = function (response) {
        that.listaassuntos=response.data;

    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/secretaria/reunioes/assuntos/salvar?reuniao_id=" + $scope.retorno + "&assunto=" + $scope.assunto;
    Ajax.request("GET", url, that, callback_success, callback_error);
  }
});
manager36App.controller('SubsedeCtrl', function($scope, Ajax) {
  $scope.estado=null;
  $scope.cidade=null;
  $scope.set_cidades = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.cidades=response.data
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/getcidadebyestado?estado=" + $scope.estado;

    Ajax.request("GET", url, that, callback_success, callback_error);
  }

  $scope.AtribuirHierarquia = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.e=response.data;
        window.location.assign('/diretoria/subsede');
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/diretoria/subsede/diretoria?cargo=" + $scope.cargo + "&integrante=" + $scope.integrante;
    Ajax.request("GET", url, that, callback_success, callback_error);
  }

  $scope.SalvarSede = function(){
    var that = $scope;
    var callback_success = function (response) {
        that.e=response.data;
        window.location.assign('/diretoria/subsede');
    }
    var callback_error = function (response) {
        console.log("Erro");
    }
    var url = "/diretoria/subsede/salvar?estado=" + $scope.estado + "&cidade=" + $scope.cidade + "&cep=" + $scope.cep + "&bairro=" + $scope.bairro + "&endereco=" + $scope.endereco + "&acomoda=" + $scope.acomoda;
    Ajax.request("GET", url, that, callback_success, callback_error);
  }
});
