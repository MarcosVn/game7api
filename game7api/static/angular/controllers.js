game7App.controller('SubCategoriaCtrl', function($scope, Ajax) {
  $scope.estado=null;
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