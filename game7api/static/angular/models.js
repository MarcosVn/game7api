URL_BASE = "http://0.0.0.0:8007/js/";

function getTokens(){
    var tokens = [];            // new array to hold result
    var query = location.search; // everything from the '?' onward
    query = query.slice(1);     // remove the first character, which will be the '?'
    query = query.split('&');   // split via each '&', leaving us an array of something=something strings

    // iterate through each something=something string
    $.each(query, function(i,value){

        // split the something=something string via '=', creating an array containing the token name and data
        var token = value.split('=');

        // assign the first array element (the token name) to the 'key' variable
        var key = decodeURIComponent(token[0]);

        // assign the second array element (the token data) to the 'data' variable
        var data = decodeURIComponent(token[1]);

        tokens[key] = data;     // add an associative key/data pair to our result array, with key names being the URI token names
    });

    return tokens;  // return the array
}

TOKENS = getTokens();


game7App.factory("Categoria", function (Ajax,$http) {
    var obj = {
        lista_categorias: [],
        lista_subcategorias:[],
        categoriaselecionado: [],
        retorno : false,
    };
    obj.get_categorias = function (nome_categoria) {
        var url = URL_BASE + "categorias";
        var params = {
            nome:nome_categoria
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_categorias = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_categoria = function () {
        //Get relação de categorias
        var url = URL_BASE + "categorias";
        var params = {
          id:TOKENS['c_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.categoriaselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });

        //Get da lista de subcategorias
        var url = URL_BASE + "subcategorias";
        var params = {
          categoria:TOKENS['c_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_subcategorias = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_categoria = function (categoria_nome) {
        var url = URL_BASE + "savecategoria";

        var f = new FormData();
        f.append('id', TOKENS['c_id']);
        f.append('nome', categoria_nome);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_categoria = function () {
        var url = URL_BASE + "excluircategoria";
        var params = {
          id:TOKENS['c_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.retorno = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});

game7App.factory("SubCategoria", function (Ajax,$http) {
    var obj = {
        lista_subcategorias: [],
        subcategoriaselecionado: [],
        retorno : false,
    };
    obj.get_subcategorias = function (nome_subcategoria) {
        var url = URL_BASE + "subcategorias";
        var params = {
            categoria:TOKENS["c_id"],
            nome:nome_subcategoria,
            id:TOKENS["subc_id"]
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_subcategorias = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_subcategoria = function () {
        //Get relação de subcategorias
        var url = URL_BASE + "subcategorias";
        var params = {
          id:TOKENS['subc_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.subcategoriaselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_subcategoria = function (subcategoria_nome) {
        var url = URL_BASE + "savesubcategoria";

        var f = new FormData();
        f.append('id', TOKENS['subc_id']);
        f.append('categoria', TOKENS['c_id']);
        f.append('nome', subcategoria_nome);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_subcategoria = function () {
        var url = URL_BASE + "excluirsubcategoria";
        var params = {
          id:TOKENS['subc_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.retorno = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});

game7App.factory("Cliente", function (Ajax,$http) {
    var obj = {
        lista_clientes: [],
        clienteselecionado: [],
        retorno : false,
    };
    obj.get_clientes = function (nome_cliente, email_cliente) {
        var url = URL_BASE + "clientes";
        var params = {
            nome:nome_cliente,
            email:email_cliente,
            id:TOKENS["c_id"]
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_subcategorias = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_cliente = function () {
        //Get relação de clientes
        var url = URL_BASE + "clientes";
        var params = {
          id:TOKENS['c_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.clienteselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_subcategoria = function (subcategoria_nome) {
        var url = URL_BASE + "savesubcategoria";

        var f = new FormData();
        f.append('id', TOKENS['subc_id']);
        f.append('categoria', TOKENS['c_id']);
        f.append('nome', subcategoria_nome);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_subcategoria = function () {
        var url = URL_BASE + "excluirsubcategoria";
        var params = {
          id:TOKENS['subc_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.retorno = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});