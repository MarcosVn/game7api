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
            scope.Pedido = Pedido;
        }
    };
});

game7App.directive("avaliacao", function($http){
    return {
        templateUrl: '/static/angular/diretivas/avaliacao.html',
        restrict: 'E',
        scope: {
            pedido_id: "@"
        },
        transclude: true,
        link: function(scope){
            scope.avaliacao = {};
            scope.tela_avaliacao = location.pathname.indexOf('avaliacao') >= 0;
            scope.menu = 'lista';
            scope.pedido = false;
            var user_id = window.localStorage.c_logado;
            //pendentes
            $http({url: "http://localhost:8000/js/avaliacao_pendente", method: "GET", params: {id: user_id}}).then(function(response){
                scope.avaliacao = response.data;
                if(scope.avaliacao){
                    scope.menu = 'cadastro';
                    if(!scope.tela_avaliacao)
                        $('.modal').modal('show');

                    if(scope.avaliacao.chegou_hora){
                        scope.avaliacao.chegou_hora = "true"
                    } else {
                        scope.avaliacao.chegou_hora = "false"
                    }
                }
                $http({url: URL_BASE + "pedidos", method: "GET", params: {id: scope.avaliacao.pedido}}).then(function(response){
                    scope.pedido = response.data[0];
                });
            });
            scope.salvar = function(){
                console.log('salvando');
                $http({url: "http://localhost:8000/js/" + "editavaliacao", method: "POST", data: scope.avaliacao});
            };
            //realizados
            $http({url: "http://localhost:8000/js/avaliacao_realizadas", method: "GET", params: {id: user_id}}).then(function(response){
                scope.avaliacao_realizadas = response.data;
            });
        }
    };
});
