var game7App = angular.module("game7App", []);
game7App.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[').endSymbol(']}');
});

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
