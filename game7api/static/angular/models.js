URL_BASE = "http://0.0.0.0:8010/js/";
//URL_BASE = "http://127.0.0.1:8000/js/";
//URL_BASE = "https://serene-atoll-63219.herokuapp.com/js/";
//URL_BASE = "http://menuweb.com.br/js/";

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
        estado_selecionado:[]
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
    obj.get_estados_by_nome= function (nome) {
        var url = URL_BASE + "estados";
        var params = {
            nome:nome
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.estado_selecionado= response.data[0];
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
        cidade_selecionado :[]
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
    obj.get_cidades_by_nome= function (nome) {
        var url = URL_BASE + "cidades";
        var params = {
            nome:nome
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.cidade_selecionado=response.data[0];
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
        bairro_selecionado: []
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
    obj.get_bairros_by_nome= function (nome) {
        var url = URL_BASE + "bairros";
        var params = {
            nome:nome
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.bairro_selecionado= response.data[0];
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
        sel_categoria:null,
        sel_subcategorias:null
    };
    obj.get_subcategorias = function (nome_subcategoria, categoria_id) {

        if ((categoria_id == undefined) || (categoria_id == 0) || (categoria_id == null))
        {
            categoria_id=TOKENS["c_id"];
        }

        var url = URL_BASE + "subcategorias";
        var params = {
            categoria:categoria_id,
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
        sel_cidade:"1"
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

    obj.get_recuperarsenha = function (email_cliente, senha_cliente) {
        var url = URL_BASE + "recuperar_cliente";

        var f = new FormData();
        f.append('token', TOKENS['key']);
        f.append('email', email_cliente);
        f.append('senha', senha_cliente);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno= response;
            alert("Senha Recuperada!");
          }
        )

    };

    obj.sair_cliente = function () {
        window.localStorage.removeItem("c_logado");
        window.location = "";

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

    obj.get_clientelogado = function () {
        //Get relação de clientes
        var url = URL_BASE + "cliente-logado";
        var params = {
          id:window.localStorage.getItem("c_logado")
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.clientelogado = response.data;

        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.save_cliente = function (cliente_nome, cliente_email, cliente_senha, cliente_telefone, cliente_estado, cliente_cidade, cliente_bairro, cliente_endereco, cliente_numero, cliente_complemento, cliente_cep) {
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
        f.append('numero', cliente_numero);
        f.append('complemento', cliente_complemento);
        f.append('cep', cliente_cep);
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
    obj.logar_cliente = function (email_cliente,senha_cliente) {
        var url = URL_BASE + "cliente-login";

        var f = new FormData();
        f.append('email', email_cliente);
        f.append('senha', senha_cliente);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            if(response.length > 0){
                obj.clientelogado = response;

                window.localStorage.setItem("c_logado", response[0].id);
            }
            else{
                alert("Usuário ou senha incorretos");
            }
          }
        )
    };

    return obj;
});

game7App.factory("Empresa", function (Ajax,$http) {
    var obj = {
        lista_empresas: [],
        lista_empresasremessas: [],
        empresaselecionado: [],
        retorno : false,
        data_fim : new Date(),
        foto_principal:123
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

    obj.get_empresarepasse = function (data_final) {
        //Get relação de clientes
        var url = URL_BASE + "empresasrepasses";
        var params = {
          id:TOKENS['e_id'],
          data_fim:data_final
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_empresasremessas = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.efetuarrepasse = function (ref, data_final) {
        //Get relação de clientes
        var url = URL_BASE + "criarrepasse";

        var f = new FormData();
        f.append('id', TOKENS['e_id']);
        f.append('referencia', ref);
        f.append('data_final', data_final);
        f.append('status', true);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )
    };

    obj.efetuarlimitacao = function (ref, data_final) {
        //Get relação de clientes
        var url = URL_BASE + "criarrepasse";

        var f = new FormData();
        f.append('id', TOKENS['e_id']);
        f.append('referencia', ref);
        f.append('data_final', data_final);
        f.append('status', false);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )
    };

    obj.receberrepasse = function (r_id) {

        var url = URL_BASE + "receberrepasse";

        var f = new FormData();
        f.append('id', r_id);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )
    };

    obj.save_empresa = function (empresa_nome, empresa_email, empresa_senha, empresa_telefone, empresa_estado, empresa_cidade, empresa_bairro, empresa_endereco, empresa_descricao, tipo_cozinha, mensalidade, porcentagem, numero, complemento, cep) {
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
        f.append('tipo_cozinha_id', tipo_cozinha);
        f.append('porcentagem_repasse', porcentagem);
        f.append('valor_mensalidade', mensalidade);
        f.append('logotipo', obj.foto_principal);
        f.append('cep', cep);
        f.append('numero', numero);
        f.append('complemento', complemento);
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
    obj.save_atendimento = function (empresa_bairro, empresa_frete) {
        var url = URL_BASE + "saveempresabairro";

        var f = new FormData();
        f.append('id', TOKENS['e_id']);
        f.append('bairro', empresa_bairro);
        f.append('frete', empresa_frete);
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
        funcionario_logado:[]
    };
    obj.logar_funcionario= function (email_funcionario,senha_funcionario) {
        var url = URL_BASE + "funcionario-login";

        var f = new FormData();
        f.append('email', email_funcionario);
        f.append('senha', senha_funcionario);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            if(response != ''){
                obj.funcionario_logado = response[0];
                obj.logado = response[0].id;
                window.localStorage.setItem("e_logado", response[0].id);
                window.location = "/adm";
            }
          }
        )
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
    obj.verifica_login = function () {
       var logado = window.localStorage.getItem("e_logado");
       var url = window.location.pathname;

       if(logado == undefined){
         window.location = "/adm/login";
       }
   };

    obj.sair = function () {
        window.localStorage.removeItem("e_logado");
        window.location = "/adm/login";
   };
    return obj;
});

game7App.factory("Produto", function (Ajax,$http) {
    var obj = {
        lista_produtos: [],
        produtoselecionado: [],
        retorno : false,
        foto_principal:123
    };
    obj.get_produtos= function (nome_produto, nome_restaurante) {
        var url = URL_BASE + "produtos";
        var params = {
            empresa_id:TOKENS["e_id"],
            nome:nome_produto,
            restaurante:nome_restaurante
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_produtos= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_produto = function () {
        //Get relação de produtos
        var url = URL_BASE + "produtos";
        var params = {
          id:TOKENS['p_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.produtoselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_produto = function (produto_nome, produto_preco, produto_descricao, empresa, subcategoria_id) {
        var url = URL_BASE + "saveproduto";

        var f = new FormData();
        f.append('id', TOKENS['p_id']);
        f.append('nome', produto_nome);
        f.append('preco', produto_preco);
        f.append('descricao', produto_descricao);
        f.append('foto', obj.foto_principal);
        f.append('empresa_id', empresa);
        f.append('subcategoria_id', subcategoria_id);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_produto= function () {
        var url = URL_BASE + "excluirproduto";
        var params = {
          id:TOKENS['p_id']
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
    obj.save_produtocategoria = function (subcategoria_id) {
        var url = URL_BASE + "saveprodutosubcategoria";

        var f = new FormData();
        f.append('id', TOKENS['p_id']);
        f.append('subcategoria_id', subcategoria_id);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_produtocategoria= function () {
        var url = URL_BASE + "excluirprodutosubcategoria";
        var params = {
          p_id:TOKENS['p_id'],
          subc_id:TOKENS['subc_id']
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
    obj.save_produtoopcional = function (opcional_id) {
        var url = URL_BASE + "saveprodutoopcional";

        var f = new FormData();
        f.append('id', TOKENS['p_id']);
        f.append('opcional_id', opcional_id);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_produtoopcional= function () {
        var url = URL_BASE + "excluirprodutoopcional";
        var params = {
          p_id:TOKENS['p_id'],
          op_id:TOKENS['op_id']
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
    obj.save_produtofoto = function (subcategoria_id) {
        var url = URL_BASE + "saveprodutofoto";

        var f = new FormData();
        f.append('id', TOKENS['p_id']);
        f.append('foto', obj.foto_principal);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_produtofoto= function (foto_id) {
        var url = URL_BASE + "excluirproduto_foto";
        var params = {
          id:TOKENS['p_id'],
          f_id:foto_id
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

game7App.factory("Pedido", function (Ajax,$http) {
    var obj = {
        lista_pedidos: [],
        pedidoselecionado: [],
        retorno : false
    };
    obj.get_pedidos= function (data_pedido, status) {
        var url = URL_BASE + "pedidos";
        var params = {
            empresa_id:TOKENS["e_id"],
            data:data_pedido,
            status:status
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_pedidos= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_pedido = function () {
        //Get relação de pedidos
        var url = URL_BASE + "pedidos";
        var params = {
          id:TOKENS['p_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.pedidoselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_pedido = function (produto_nome, produto_preco, produto_descricao, empresa) {
        var url = URL_BASE + "savepedido";

        var f = new FormData();
        f.append('id', TOKENS['p_id']);
        f.append('nome', produto_nome);
        f.append('preco', produto_preco);
        f.append('descricao', produto_descricao);
        f.append('foto', obj.foto_principal);
        f.append('empresa_id', empresa);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_produto= function () {
        var url = URL_BASE + "excluirproduto";
        var params = {
          id:TOKENS['p_id']
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


game7App.factory("Mensalidade", function (Ajax,$http) {
    var obj = {
        lista_mensalidades: [],
        mensalidadeselecionado: [],
        retorno : false,
    };
    obj.get_mensalidades = function (data_mensalidade, status_mensalidade) {
        var url = URL_BASE + "mensalidades";
        var params = {
            data:data_mensalidade,
            status:status_mensalidade
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_mensalidades=response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.gerar_mensalidade = function (id_empresa) {
        var url = URL_BASE + "savemensalidade";

        var f = new FormData();
        f.append('empresa_id', id_empresa);
        f.append('id', 0);
        f.append('status', 'Aguardando Pagamento');
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno= response;
            obj.get_mensalidades();
          }
        )
    };

    obj.receber_mensalidade = function (id_mensalidade) {
        var url = URL_BASE + "savemensalidade";

        var f = new FormData();
        f.append('empresa_id', 0);
        f.append('id', id_mensalidade);
        f.append('status', 'Pago');
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno= response;
            obj.get_mensalidades();
          }
        )
    };

    obj.cancelar_mensalidade = function (id_mensalidade) {

        var url = URL_BASE + "savemensalidade";

        var f = new FormData();
        f.append('empresa_id', 0);
        f.append('id', id_mensalidade);
        f.append('status', 'Cancelado');
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno= response;
            obj.get_mensalidades();
          }
        )

        //Get relação de clientes
//        var url = URL_BASE + "excluirmensalidade";
//        var params = {
//          id:id
//        }
//        $http({
//            method: "GET",
//            params: params,
//            url: url,
//            headers: {
//                'Content-Type': 'application/json'
//            }
//        }).then(function successCallback(response) {
//            obj.retorno= response;
//        }, function errorCallback(response) {
//            console.log("Erro");
//        });
    };

    return obj;
});

game7App.factory("TipoCozinha", function (Ajax,$http) {
    var obj = {
        lista_tiposcozinha: [],
        tipocozinhaselecionado: [],
        retorno : false,
    };
    obj.get_tiposcozinha = function (nome_tipocozinha) {
        var url = URL_BASE + "tiposcozinhas";
        var params = {
            nome:nome_tipocozinha
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_tiposcozinha = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_tipocozinha = function () {
        var url = URL_BASE + "tiposcozinhas";
        var params = {
          id:TOKENS['t_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.tipocozinhaselecionado = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_tipocozinha = function (tipocozinha_nome) {
        var url = URL_BASE + "savetipocozinha";

        var f = new FormData();
        f.append('id', TOKENS['t_id']);
        f.append('nome', tipocozinha_nome);
        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_tipocozinha = function () {
        var url = URL_BASE + "excluirtipocozinha";
        var params = {
          id:TOKENS['t_id']
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


game7App.factory("Opcional", function (Ajax,$http) {
    var obj = {
        lista_opcionais: [],
        opcionalselecionado: [],
        retorno : false,
    };
    obj.get_opcionais = function (titulo_opcional) {
        var url = URL_BASE + "opcionais";
        var params = {
            titulo:titulo_opcional,
            empresa_id:TOKENS['e_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_opcionais = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_opcional = function () {
        var url = URL_BASE + "opcionais";
        var params = {
          id:TOKENS['o_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.opcionalselecionado= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_opcional = function (empresa_selecionado, opcional_titulo, opcional_quantitativo, opcional_unico) {
        var url = URL_BASE + "saveopcional";

        var f = new FormData();
        f.append('id', TOKENS['o_id']);
        f.append('titulo', opcional_titulo);
        f.append('quantitativo', opcional_quantitativo);
        f.append('unico', opcional_unico);
        f.append('empresa_id', empresa_selecionado);

        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_opcional = function () {
        var url = URL_BASE + "excluiropcional";
        var params = {
          id:TOKENS['o_id']
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


game7App.factory("Opcao", function (Ajax,$http) {
    var obj = {
        lista_opcoes: [],
        opcaoselecionado: [],
        retorno : false,
    };
    obj.get_opcoes = function (titulo_opcional) {
        var url = URL_BASE + "opcoes";
        var params = {
            titulo:titulo_opcional,
            empresa_id:TOKENS['o_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.lista_opcoes = response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };

    obj.get_opcao = function () {
        var url = URL_BASE + "opcoes";
        var params = {
          id:TOKENS['oa_id']
        }
        $http({
            method: "GET",
            params: params,
            url: url,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function successCallback(response) {
            obj.opcaoselecionado= response.data;
        }, function errorCallback(response) {
            console.log("Erro");
        });
    };
    obj.save_opcao = function (opcao_titulo, opcao_valor) {
        var url = URL_BASE + "saveopcao";

        var f = new FormData();
        f.append('opcional_id', TOKENS['o_id']);
        f.append('titulo', opcao_titulo);
        f.append('valor', opcao_valor);


        $http.post(url, f, {headers: {'Content-Type': undefined}}).success(
          function(response){
            obj.retorno = response;
          }
        )

    };
    obj.excluir_opcao = function () {
        var url = URL_BASE + "excluiropcao";
        var params = {
          id:TOKENS['oa_id']
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