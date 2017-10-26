game7App.directive("pagamento", function(Pedido){
    return {
        templateUrl: '/static/angular/diretivas/cliente-realizar-pedido-pagamento.html',
        restrict: 'A',
        transclude: true,
        link: function(scope){
            scope.Pedido = Pedido;
            scope.ola = function(){
                console.log(scope.Cena);
            };
        }
    };
});

game7App.directive("naentrega", function(Pedido){
    return {
        templateUrl: '/static/angular/diretivas/cliente-realizar-pedido-pagamento-naentrega.html',
        restrict: 'A',
        scope: {
            tipo: "@"
        },
        transclude: true,
        link: function(scope){
            console.log('scope.tipo');
            console.log(scope.tipo);
            scope.Pedido = Pedido;
            scope.ola = function(){
                console.log(scope.Cena);
            };
        }
    };
});
