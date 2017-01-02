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

game7App.factory("Estado", function (Ajax,$http) {
    var obj = {
        lista_estados: [],
        retorno : false,
    };
    obj.get_estados= function () {
        var url = URL_BASE + "estados";
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
            obj.lista_estados= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});

game7App.factory("Cidade", function (Ajax,$http) {
    var obj = {
        lista_cidades: [],
        retorno : false,
    };
    obj.get_cidades= function (estado_id) {
        var url = URL_BASE + "cidades";
        var params = {
            estado_id:estado_id,
            id:TOKENS["cid_id"]
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_cidades= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});

game7App.factory("Bairro", function (Ajax,$http) {
    var obj = {
        lista_bairros: [],
        retorno : false,
    };
    obj.get_bairros= function (cidade_id) {
        var url = URL_BASE + "bairros";
        var params = {
            cidade_id:cidade_id,
            id:TOKENS["bai_id"]
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_bairros= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    return obj;
});

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
            obj.lista_clientes= response.data;
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
    obj.save_cliente = function (cliente_nome, cliente_email, cliente_senha, cliente_telefone, cliente_estado, cliente_cidade, cliente_bairro, cliente_endereco) {
        var url = URL_BASE + "savecliente";

        var f = new FormData();
        f.append('id', TOKENS['c_id']);
        f.append('nome', cliente_nome);
        f.append('email', cliente_email);
        f.append('senha', cliente_senha);
        f.append('telefone', cliente_telefone);
        f.append('estado', cliente_estado);
        f.append('cidade', cliente_cidade);
        f.append('bairro', cliente_bairro);
        f.append('endereco', cliente_endereco);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_cliente= function () {
        var url = URL_BASE + "excluircliente";
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

game7App.factory("Empresa", function (Ajax,$http) {
    var obj = {
        lista_empresas: [],
        empresaselecionado: [],
        retorno : false,
    };
    obj.get_empresas = function (nome_empresa, email_empresa) {
        var url = URL_BASE + "empresas";
        var params = {
            nome:nome_empresa,
            email:email_empresa,
            id:TOKENS["e_id"]
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_empresas= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_empresa = function () {
        //Get relação de clientes
        var url = URL_BASE + "empresas";
        var params = {
          id:TOKENS['e_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.empresaselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_empresa = function (empresa_nome, empresa_email, empresa_senha, empresa_telefone, empresa_estado, empresa_cidade, empresa_bairro, empresa_endereco, empresa_descricao) {
        var url = URL_BASE + "saveempresa";

        var f = new FormData();
        f.append('id', TOKENS['e_id']);
        f.append('nome', empresa_nome);
        f.append('email', empresa_email);
        f.append('senha', empresa_senha);
        f.append('telefone', empresa_telefone);
        f.append('estado', empresa_estado);
        f.append('cidade', empresa_cidade);
        f.append('bairro', empresa_bairro);
        f.append('endereco', empresa_endereco);
        f.append('descricao', empresa_descricao);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )
    };
    obj.excluir_empresa= function () {
        var url = URL_BASE + "excluirempresa";
        var params = {
          id:TOKENS['e_id']
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

game7App.factory("Atendimento", function (Ajax,$http) {
    var obj = {
        retorno : false,
    };
    obj.save_atendimento = function (empresa_bairro) {
        var url = URL_BASE + "saveempresabairro";

        var f = new FormData();
        f.append('id', TOKENS['e_id']);
        f.append('bairro', empresa_bairro);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )
    };
    obj.excluir_atendimento= function () {
        var url = URL_BASE + "excluirempresa_bairro";
        var params = {
          empresa_id:TOKENS['e_id'],
          bairro_id:TOKENS['b_id']
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

game7App.factory("Funcionario", function (Ajax,$http) {
    var obj = {
        lista_funcionarios: [],
        funcionarioselecionado: [],
        retorno : false,
    };
    obj.get_funcionarios = function (nome_funcionario, email_funcionario) {
        var url = URL_BASE + "funcionarios";
        var params = {
            nome:nome_funcionario,
            email:email_funcionario
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_funcionarios= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_funcionario = function () {
        //Get relação de funcionarios
        var url = URL_BASE + "funcionarios";
        var params = {
          funcionario_id:TOKENS['f_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.funcionarioselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_funcionario = function (funcionario_nome, funcionario_email, funcionario_senha, funcionario_telefone, funcionario_endereco) {
        var url = URL_BASE + "savefuncionario";

        var f = new FormData();
        f.append('id', TOKENS['f_id']);
        f.append('nome', funcionario_nome);
        f.append('email', funcionario_email);
        f.append('senha', funcionario_senha);
        f.append('telefone', funcionario_telefone);
        f.append('endereco', funcionario_endereco);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_funcionario= function () {
        var url = URL_BASE + "excluirfuncionario";
        var params = {
          id:TOKENS['f_id']
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
