var game7App = angular.module("game7App", []);
game7App.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[').endSymbol(']}');
});

game7App.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }
]);

game7App.service("Ajax", function($http){
    return {
        request:function (method, url, data, callback_success, callback_error) {
            $http({
                method: method,
                params: data,
                url: url,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function successCallback(response) {
                callback_success(response);
            }, function errorCallback(response) {
                callback_error(response);
            });
        }
    }
});
